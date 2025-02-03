import numpy as np
import pandas as pd
from typing import List, Dict

def recommend_content_based(content_based_model, user_tag_scores: Dict[str, float], attraction_data: List[List[float]], attraction_refs: List[tuple]) -> List[str]:
    user_vector = np.array(list(user_tag_scores.values())).reshape(1, -1)
    distances, indices = content_based_model.kneighbors(user_vector)
    recommendations = [attraction_refs[idx][0] for idx in indices[0]]
    return recommendations

def recommend_collaborative(collaborative_model, ratings_matrix: pd.DataFrame, user_id: str) -> List[str]:
    # Find the user's ratings
    row_position = ratings_matrix.index.get_loc(user_id)
    # Get 10 neighbors(10 similar user)
    user_rating_vector = ratings_matrix.iloc[row_position, :].values.reshape(1,-1)
    distances, indices = collaborative_model.kneighbors(user_rating_vector, n_neighbors=10+1)

    # Get similar users(exclude the target user itself)
    similar_users = indices.flatten()
    similar_users = similar_users[similar_users != row_position]

    # Aggregate attraction ratings from similar users
    similar_users_ratings = ratings_matrix.iloc[similar_users].mean(axis=0)

    # Exclude already rated attractions by the user
    user_ratings = ratings_matrix.iloc[row_position]
    recommendations = similar_users_ratings[user_ratings == 0]

    # Sort recommendations by highest score
    recommendations = recommendations.sort_values(ascending=False)

    return recommendations