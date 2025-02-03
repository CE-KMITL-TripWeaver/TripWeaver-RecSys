import pandas as pd
import numpy as np
import json
import requests
import ast
import math
from sklearn.neighbors import NearestNeighbors

import joblib


'''
This script is used to retrain Content-based model (run when start container)
so all paths must fit the Docker container directory
'''

# get attractions data
attraction_tag_score_data = []
attraction_ref = []
try:
    # API_ENDPOINT = "http://localhost:3000/api/attraction/getAllData"
    API_ENDPOINT = "http://tripweaver:3000/api/attraction/getAllData" #use this if run in docker container
    res_all_attractions = requests.post(url=API_ENDPOINT).json()
    
    for cur_attraction in res_all_attractions['attractions']:
        cur_tag_score = cur_attraction['attractionTag']['attractionTagFields']
        cur_ref = (cur_attraction['_id'], cur_attraction['name'])

        attraction_tag_score_data.append(list(cur_tag_score.values()))
        attraction_ref.append(cur_ref)

    # train KNN Model
    attraction_tag_score_matrix = np.array(attraction_tag_score_data.copy())
    knn = NearestNeighbors(n_neighbors=30, metric='cosine') # euclidean, cosine
    knn.fit(attraction_tag_score_matrix)

    # save model to api/Hybrid_Recommendation_System (chage path to corresponded docker container)
    joblib.dump(knn, './models/model_content-based.joblib')
        
except Exception as e:
    print("retrain content-based failed !")
    print(e)