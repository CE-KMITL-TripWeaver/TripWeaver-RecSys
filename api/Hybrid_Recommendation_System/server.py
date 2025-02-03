from fastapi import FastAPI, HTTPException
from typing import List, Dict, Tuple
import joblib
from sklearn.neighbors import NearestNeighbors
import google.generativeai as genai
from google.generativeai.types import ContentType
from PIL import Image
from IPython.display import Markdown
import numpy as np
import pandas as pd
import json
import requests
import os
import glob
import datetime
from dotenv import load_dotenv

# "sys.path" is a list that contains directories where Python looks for modules when you use "import"
import sys
sys.path.append('.')
sys.path.append('../../')

from services.recommendation import recommend_content_based, recommend_collaborative
from services.attraction_data import fetch_attraction_data, preprocess_attraction_data
from services.user_rating_data import fetch_user_rating_data, preprocess_user_rating_data
from schemas.recommendation import RecommendationResponse

from packages.file_handler_package.file_handler import *


path_to_model_content_based = "./models/model_content-based.joblib"
model_content_based = joblib.load(path_to_model_content_based)

path_to_model_collaborative = "./models/model_collaborative_filtering.joblib"
model_collaborative = joblib.load(path_to_model_collaborative)

load_dotenv() 

app = FastAPI()

# Health check endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the Attraction Recommendation API"}

# generate attraction tags for a new user (after answering preference questions)
@app.post("/generate-user-tagScore")
def generate_user_attractionTag(user_preference_prompt: Dict):
    """
    Retrieves tag scores for a user based on their responses during the sign-up process using the Gemini API.

    Args:
        user_preference_prompt (Dict): A dictionary representing the list of user's responses to each question

    Returns:
        Dictionary representing scores for all tags.
    """

    # configure the Gemini API model
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
    model = genai.GenerativeModel('gemini-1.5-flash-latest')
    
    # construct the base prompt
    text_prompt = (
        "Based on the user's answers, generate a JSON string containing scores (0-1) for the following attributes (nothing else, no other sentences):"
        "\nExample JSON: "
        '{"Tourism":0,"Adventure":0,"Meditation":0,"Art":0,"Cultural":0,"Landscape":0,"Nature":0,"Historical":0,'
        '"Cityscape":0,"Beach":0,"Mountain":0,"Architecture":0,"Temple":0,"WalkingStreet":0,"Market":0,'
        '"Village":0,"NationalPark":0,"Diving":0,"Snuggle":0,"Waterfall":0,"Island":0,"Shopping":0,'
        '"Camping":0,"Fog":0,"Cycling":0,"Monument":0,"Zoo":0,"Waterpark":0,"Hiking":0,"Museum":0,'
        '"Riverside":0,"NightLife":0,"Family":0,"Kid":0,"Landmark":0,"Forest":0}'
    )

    # Add each question and its corresponding score to the prompt
    for item in user_preference_prompt["preference_prompt"]:
        question = item["question"]
        score = item["score"]
        text_prompt += f"\nQuestion: {question}\nUser Answer: {score}/5"

    prompt = [text_prompt]

    # send the prompt to the Gemini API
    res_score_dict = {}
    try:
        response = model.generate_content(prompt)
        res_start_Idx = response.text.find('{')
        res_end_Idx = response.text.find('}')
        res_score_dict =  json.loads(response.text[res_start_Idx:res_end_Idx+1])

    except Exception as e:
        print("failed to use gemini api")
    
    return res_score_dict

# generate attraction tags for a new created attraction
@app.post("/generate-attraction-tagScore")
def generate_attractionTag(attraction_data: Dict):
    """
    Generates tag scores for a newly created attraction based on its properties, such as image address, name, and latitude/longitude, using the Gemini API.

    Args:
        attraction_data (Dict): A dictionary representing the attraction's details.

    Returns:
        Dictionary representing scores for all tags.
    """

    # create a 'temp' directory to store temporarily downloaded images, which will be used in requests to the Gemini API
    cur_dir = os.getcwd()
    createDirectory(cur_dir, 'temp')

    name = attraction_data['name']
    all_img_url = attraction_data['imgPath']
    latitude = attraction_data['latitude']
    longitude= attraction_data['longitude']

    for Idx, cur_url in enumerate(all_img_url):
        if(cur_url == '' or Idx == 3):
            break
        response = requests.get(cur_url)
        if response.status_code == 200:
            filename = 'temp/temp_img_{0}.jpeg'.format(Idx)
            with open(filename, 'wb') as file:
                file.write(response.content)

    # send API request to retrieve the score for the current attraction (including a query and the main image).
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
    model = genai.GenerativeModel('gemini-1.5-flash-latest')
    # model = genai.GenerativeModel('gemini-1.5-pro-latest')
    
    text_prompt = "Provide place name, latitude, and longitude. I will return a JSON string containing scores (0-1) for following attributes(nothing else no other sentences)" + \
    "\nfor example: \'{\"Tourism\":0,\"Adventure\":0,\"Meditation\":0,\"Art\":0,\"Cultural\":0,\"Landscape\":0,\"Nature\":0,\"Historical\":0,\"Cityscape\":0,\"Beach\":0,\"Mountain\":0,\"Architecture\":0,\"Temple\":0,\"WalkingStreet\":0,\"Market\":0,\"Village\":0,\"NationalPark\":0,\"Diving\":0,\"Snuggle\":0,\"Waterfall\":0,\"Island\":0,\"Shopping\":0,\"Camping\":0,\"Fog\":0,\"Cycling\":0,\"Monument\":0,\"Zoo\":0,\"Waterpark\":0,\"Hiking\":0,\"Museum\":0,\"Riverside\":0,\"NightLife\":0,\"Family\":0,\"Kid\":0,\"Landmark\":0,\"Forest\":0}" + \
    "\n{0}, {1}, {2} give me score for this".format(name, latitude, longitude)

    # send a prompt to the model
    prompt = [text_prompt]
    for Idx, cur_path_img in enumerate(glob.glob(os.path.join(cur_dir, 'temp', '*.jpeg'))):
        # use a maximum of 3 images in the prompt to reduce token usage.
        if(Idx == 3):
            break
        cur_img_prompt = Image.open(cur_path_img)
        prompt.append(cur_img_prompt)
        
    res_score_dict = {}
    try:
        response = model.generate_content(prompt)
        # remove directory 'temp'
        removeNoneEmptyDir(os.path.join(cur_dir, 'temp'))
        res_start_Idx = response.text.find('{')
        res_end_Idx = response.text.find('}')
        res_score_dict =  json.loads(response.text[res_start_Idx:res_end_Idx+1])

    except Exception as e:
        # remove directory 'temp'
        removeNoneEmptyDir(os.path.join(cur_dir, 'temp'))
        print("failed to use gemini api")
    
    return res_score_dict

# retrain model (content-based)
@app.post("/retrain-model-content-based")
def retrain_model_content_based():
    global model_content_based  # update global variable

    print(f"Retrain model content-based --> {datetime.datetime.now()}")
    try:
        api_endpoint = "http://localhost:3000/api/attraction/getAllData"
        # api_endpoint = "http://tripweaver:3000/api/attraction/getAllData" # use this if run in docker container
        res_all_attractions = fetch_attraction_data(api_endpoint)

        attraction_tag_score_data, attraction_ref = preprocess_attraction_data(res_all_attractions)
        attraction_tag_score_matrix = np.array(attraction_tag_score_data.copy())
        knn = NearestNeighbors(n_neighbors=30, metric='cosine')
        knn.fit(attraction_tag_score_matrix)

        # save model to api/Hybrid_Recommendation_System (chage path to corresponded docker container)
        joblib.dump(knn, path_to_model_content_based)

        # reload updated model
        model_content_based = joblib.load(path_to_model_content_based)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Retrain model content-based process failed: {e}")
    
    return {"message": "Content-based model retrained successfully"}

# retrain model (collaborative)
@app.post("/retrain-model-collaborative")
def retrain_model_collaborative():
    global model_collaborative  # update global variable

    print(f"Retrain model collaborative --> {datetime.datetime.now()}")
    try:
        api_endpoint = "http://localhost:3000/api/userrating/getAll"
        # api_endpoint = "http://tripweaver:3000/api/userrating/getAll" # use this if run in docker container
        res_all_user_rating = fetch_user_rating_data(api_endpoint)

        ratings_matrix = preprocess_user_rating_data(res_all_user_rating)
        knn = NearestNeighbors(metric='cosine')
        knn.fit(ratings_matrix)

        # save model to api/Hybrid_Recommendation_System (chage path to corresponded docker container)
        joblib.dump(knn, path_to_model_collaborative)

        # reload updated model
        model_collaborative = joblib.load(path_to_model_collaborative)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Retrain model collaborative process failed: {e}")
    
    return {"message": "Collaborative model retrained successfully"}


# recommend attraction using model content-based
@app.post("/recommend-content-based")
def recommend_attractions(user: Dict):
    ''' 
    reccomend attraction by content based model
    ''' 

    try:
        # reccomend by content based model
        print(f"Reccomend by content-based --> {datetime.datetime.now()}")
        api_endpoint = "http://localhost:3000/api/attraction/getAllData"
        # api_endpoint = "http://tripweaver:3000/api/attraction/getAllData" # use this if run in docker container
        res_all_attractions = fetch_attraction_data(api_endpoint)

        attraction_tag_score_data, attraction_ref = preprocess_attraction_data(res_all_attractions)
        res_recommendation = recommend_content_based(
            model_content_based = model_content_based,
            user_tag_scores = user["attractionTagScore"]["attractionTagFields"],
            attraction_data = attraction_tag_score_data,
            attraction_refs = attraction_ref,
        )
        return {"res_recommendation": res_recommendation}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Recommendation process failed: {e}")
    

# recommend attraction using model collaborative
@app.post("/recommend-collaborative")
def recommend_attractions(user: Dict):
    ''' 
    reccomend attraction by collaborative filtering model 
    ''' 

    try:
        print(f"Reccomend by collaborative --> {datetime.datetime.now()}")
        api_endpoint = "http://localhost:3000/api/userrating/getAll"
        # api_endpoint = "http://tripweaver:3000/api/userrating/getAll" # use this if run in docker container
        res_all_user_rating = fetch_user_rating_data(api_endpoint)
        
        ratings_matrix = preprocess_user_rating_data(res_all_user_rating)
        res_recommendation = recommend_collaborative(
            model_collaborative = model_collaborative,
            ratings_matrix = ratings_matrix,
            user_id = user["_id"]
        )
        return {"res_recommendation": res_recommendation}
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Recommendation process failed: {e}")

# recommend attraction using hybrid recommendation system
@app.post("/recommend-hybrid")
def recommend_attractions(user: Dict):
    ''' 
    reccomend attraction by either content based or collaborative filtering model
    based on user's condition 
    ''' 

    try:
        # find wheter to use which model

        # recommend by collaborative filtering model
        if(True):
            print(f"Reccomend by collaborative --> {datetime.datetime.now()}")
            api_endpoint = "http://localhost:3000/api/userrating/getAll"
            # api_endpoint = "http://tripweaver:3000/api/userrating/getAll" # use this if run in docker container
            res_all_user_rating = fetch_user_rating_data(api_endpoint)
            
            ratings_matrix = preprocess_user_rating_data(res_all_user_rating)
            res_recommendation = recommend_collaborative(
                model_collaborative = model_collaborative,
                ratings_matrix = ratings_matrix,
                user_id = user["_id"]
            )
            return {"res_recommendation": res_recommendation}
        
        # reccomend by content based model
        elif(False):
            print(f"Reccomend by content-based --> {datetime.datetime.now()}")
            api_endpoint = "http://localhost:3000/api/attraction/getAllData"
            # api_endpoint = "http://tripweaver:3000/api/attraction/getAllData" # use this if run in docker container
            res_all_attractions = fetch_attraction_data(api_endpoint)

            attraction_tag_score_data, attraction_ref = preprocess_attraction_data(res_all_attractions)
            res_recommendation = recommend_content_based(
                model_content_based = model_content_based,
                user_tag_scores = user["attractionTagScore"]["attractionTagFields"],
                attraction_data = attraction_tag_score_data,
                attraction_refs = attraction_ref,
            )
            return {"res_recommendation": res_recommendation}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Recommendation process failed: {e}")