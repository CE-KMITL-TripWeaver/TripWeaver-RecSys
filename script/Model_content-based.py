import sys
import os
import glob

sys.path.append('.')

import constants.file_handler_constants as fh
from constants.user_constants import *
from constants.attraction_constants import *
from dotenv import load_dotenv
import time
import pandas as pd
import numpy as np
import json
import requests
import ast
import math
from sklearn.neighbors import NearestNeighbors

import joblib

# get a user data (if user api cannot be used)
# user_tag_score_vector = np.array(MOCK_USER[1])

'''
example user id of following persona:
- user_persona_nature --> 677e41b2519209b0aaff4d76, 677e41b6519209b0aaff4d7b
- user_persona_temple_historical --> 677e425a519209b0aaff4dda, 677e425d519209b0aaff4ddf
- user_persona_adventure --> 677e4327519209b0aaff4e3e, 677e432a519209b0aaff4e43
- user_persona_art --> 677e544b519209b0aaff4fd6, 677e544e519209b0aaff4fdb
'''

user_id = '677e4327519209b0aaff4e3e'

# Load environment variables from .env file
load_dotenv()

try:
    API_ENDPOINT = f"{os.environ['TRIPWEAVER_API']}/api/user/getUser/{user_id}"
    headers = {
        "Authorization": f"{os.environ['AUTH_BRANCH_API_KEY']}",
        "Content-Type": "application/json"
    }

    res_user = requests.get(url=API_ENDPOINT, headers=headers).json()
    user_tag_score_response = res_user['attractionTagScore']['attractionTagFields']
    user_tag_score_vector = np.array(list(user_tag_score_response.values()))

except Exception as e:
    print("GET api failed at user id --> ", user_id)
    print(e)

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
    print(e)

for cur_tag, cur_ref in zip(attraction_tag_score_data, attraction_ref):
    print(cur_ref)
    print(cur_tag)

# train KNN Model
attraction_tag_score_matrix = np.array(attraction_tag_score_data.copy())
knn = NearestNeighbors(n_neighbors=30, metric='cosine') # euclidean, cosine
knn.fit(attraction_tag_score_matrix)

# find top recommendations
user_tag_score_vector = user_tag_score_vector.reshape(1, -1)
distances, indices = knn.kneighbors(user_tag_score_vector)

print(distances)
print(indices)

print("Top Recommendations:")
for i, idx in enumerate(indices[0]):
    print(f"{i+1}. {attraction_ref[idx][1]} (Similarity: {1 - distances[0][i]:.2f})")

# save model to api/Hybrid_Recommendation_System
joblib.dump(knn, './api/Hybrid_Recommendation_System/model_content-based.joblib')