import joblib
import numpy as np
import pandas as pd
import requests
from fastapi import FastAPI, HTTPException
import os

import sys
sys.path.append('.')
from services.recommendation import recommend_content_based
from services.attraction_data import fetch_attraction_data, preprocess_attraction_data
from schemas.recommendation import RecommendationResponse

path_to_model_content_based = "./models/model_content-based.joblib"
content_based_model = joblib.load(path_to_model_content_based)

app = FastAPI()

# Health check endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the Attraction Recommendation API"}

# generate attraction tags for a new user (after answering preference questions)
@app.post("/generate-user-attractionTag")
def recommend_attractions(user: dict):
    pass

# generate attraction tags for a new created attraction
@app.post("/generate-attractionTag")
def recommend_attractions(user: dict):
    pass

# retrain model (content-based)
@app.post("/retrain-model-content-based")
def recommend_attractions(user: dict):
    pass

# retrain model (collaborative)
@app.post("/retrain-model-collaborative")
def recommend_attractions(user: dict):
    pass

# recommend attraction using hybrid recommendation system
@app.post("/recommend")
def recommend_attractions(user: dict):
    ''' 
    reccomend attraction by either content based or collaborative filtering model
    based on user's condition 
    ''' 

    try:
        # find wheter to use which model

        # recommend by collaborative filtering model
        if(False):
            pass
        
        # reccomend by content based model
        elif(True):
            # api_endpoint = "http://localhost:3000/api/attraction/getAllData"
            api_endpoint = "http://tripweaver:3000/api/attraction/getAllData" # use this if run in docker container
            res_all_attractions = fetch_attraction_data(api_endpoint)
            
            attraction_tag_score_data, attraction_ref = preprocess_attraction_data(res_all_attractions)
            res_recommendation = recommend_content_based(
                user["attractionTagScore"]["attractionTagFields"],
                content_based_model,
                attraction_tag_score_data,
                attraction_ref,
            )
            return {"res_recommendation": res_recommendation}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Recommendation process failed: {e}")