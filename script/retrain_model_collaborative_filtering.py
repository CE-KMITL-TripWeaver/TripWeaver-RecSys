import pandas as pd
import numpy as np
import os
from dotenv import load_dotenv
import json
import requests
import ast
import math
from sklearn.neighbors import NearestNeighbors
import joblib

'''
This script is used to retrain Collaborative model (run when start container)
so all paths must fit the Docker container directory
'''

load_dotenv()

user_rating_data = [] # [[user_id_1, attraction_id_1, rating],...]
try:
    API_ENDPOINT = f"{os.getenv('TRIPWEAVER_API')}/api/userrating/getAll"
    res_user_rating = requests.get(url=API_ENDPOINT).json()

    for cur_res_user_rating in res_user_rating:
        cur_user_id = cur_res_user_rating['userId']

        # users with fewer than 35 ratings have no influence on this model.
        if(len(cur_res_user_rating['rating']) < 35):
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

    knn = NearestNeighbors(metric='cosine')
    knn.fit(ratings_matrix)

    # save model to api/Hybrid_Recommendation_System (chage path to corresponded docker container)
    joblib.dump(knn, './models/model_collaborative_filtering.joblib')

except Exception as e:
    print("retrain collaborative failed !")
    print(e)