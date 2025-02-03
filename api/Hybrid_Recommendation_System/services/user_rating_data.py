import requests
import pandas as pd
from fastapi import HTTPException
from typing import List, Dict, Tuple

def fetch_user_rating_data(api_endpoint: str) -> List[Dict]:
    try:
        response = requests.get(api_endpoint).json()
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch user rating data: {e}")

def preprocess_user_rating_data(user_rating: List[Dict]) -> pd.DataFrame:
    user_rating_data = [] # [[user_id_1, attraction_id_1, rating],...]
    for cur_res_user_rating in user_rating:
        cur_user_id = cur_res_user_rating['userId']

        # user with no rating have no influence on this model
        if(not len(cur_res_user_rating['rating'])):
            continue
        
        for cur_user_rating in cur_res_user_rating['rating']:
            
            cur_attraction_id = cur_user_rating['attractionId']
            cur_rating_score = cur_user_rating['rating_score']

            user_rating_data.append([cur_user_id, cur_attraction_id, cur_rating_score])
    
    df = pd.DataFrame(user_rating_data, columns=['user_id', 'attraction_id', 'rating_score'])
    # Rows = Users, Columns = Attractions
    ratings_matrix = df.pivot_table(
        values = ['rating_score'], 
        index = ['user_id'],
        columns = ['attraction_id'],
        aggfunc='last',
        fill_value=0
    )
    
    return ratings_matrix