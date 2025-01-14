import joblib
import numpy as np
import pandas as pd
import requests
from fastapi import FastAPI
import os

path_to_model_content_based = "model_content-based.joblib"
content_based_model = joblib.load(path_to_model_content_based)

app = FastAPI()

# Health check endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the Attraction Recommendation API"}

@app.post("/recommend")
def recommend_attractions(user: dict):
    ''' 
    reccomend attraction by either content based or collaborative filtering model
    based on user's condition 
    ''' 

    print(type(user))
    print(user)
    print("check env")
    print(os.environ['TRIPWEAVER_API'])
    print("---")
    # find wheter to use which model

    # recommend by collaborative filtering model
    if(False):
        pass
    
    # reccomend by content based model
    elif(True):
        # get attractions data
        attraction_tag_score_data = []
        attraction_ref = []
        try:
            API_ENDPOINT = f"{os.environ['TRIPWEAVER_API']}/api/attraction/getAllData"
            res_all_attractions = requests.post(url=API_ENDPOINT).json()
            
            for cur_attraction in res_all_attractions['attractions']:
                cur_tag_score = cur_attraction['attractionTag']['attractionTagFields']
                cur_ref = (cur_attraction['_id'], cur_attraction['name'])

                attraction_tag_score_data.append(list(cur_tag_score.values()))
                attraction_ref.append(cur_ref)
                
        except Exception as e:
            print("get all attraction data failed !")

        # preprocess user data
        user_tag_score_response = user['attractionTagScore']['attractionTagFields']
        user_tag_score_vector = np.array(list(user_tag_score_response.values()))

        user_tag_score_vector = user_tag_score_vector.reshape(1, -1)
        distances, indices = content_based_model.kneighbors(user_tag_score_vector)

        print(distances)
        print(indices)

        # Print the recommendations before normalize to  [0, 0.05, 0.1, 0.15, 0.2, 0.25, ...., 0.95, 1]
        res_rec_by_norm = [] 
        print("Top Recommendations:")
        for i, idx in enumerate(indices[0]):
            print(f"{i+1}. {content_based_model[idx][1]} (Similarity: {1 - distances[0][i]:.2f})")

    return {"test": "Hello World"}