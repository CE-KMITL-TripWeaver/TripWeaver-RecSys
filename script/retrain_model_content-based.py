import sys
import os
import glob

import time
import pandas as pd
import numpy as np
import json
import requests
import ast
import math
from sklearn.neighbors import NearestNeighbors

import joblib


'''
This script is use to retrain Content-based reccemendersystem model
so all the paths have to fit docker container directory
'''

# get attractions data
attraction_tag_score_data = []
attraction_ref = []
try:
    API_ENDPOINT = "http://tripweaver:3000/api/attraction/getAllData" #use this if run in docker container
    res_all_attractions = requests.post(url=API_ENDPOINT).json()
    
    for cur_attraction in res_all_attractions['attractions']:
        cur_tag_score = cur_attraction['attractionTag']['attractionTagFields']
        cur_ref = (cur_attraction['_id'], cur_attraction['name'])

        attraction_tag_score_data.append(list(cur_tag_score.values()))
        attraction_ref.append(cur_ref)
        
except Exception as e:
    print("get all attraction data failed !")
    print(e)

for cur_tag, cur_ref in zip(attraction_tag_score_data, attraction_ref):
    print(cur_ref)
    print(cur_tag)

# train KNN Model
attraction_tag_score_matrix = np.array(attraction_tag_score_data.copy())
knn = NearestNeighbors(n_neighbors=30, metric='cosine') # euclidean, cosine
knn.fit(attraction_tag_score_matrix)


# save model to api/Hybrid_Recommendation_System (chage path to corresponded docker container)
joblib.dump(knn, './44model_content-based.joblib')