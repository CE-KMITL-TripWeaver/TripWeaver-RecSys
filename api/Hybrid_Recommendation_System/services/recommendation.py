import numpy as np
from typing import List, Dict

def recommend_content_based(user_tag_scores: Dict[str, float], content_based_model, attraction_data: List[List[float]], attraction_refs: List[tuple]):
    user_vector = np.array(list(user_tag_scores.values())).reshape(1, -1)
    distances, indices = content_based_model.kneighbors(user_vector)
    
    print("Top Recommendations (content-based):")
    recommendations = [
        {
            "id": attraction_refs[idx][0],
            "name": attraction_refs[idx][1],
            "sim_score": round(1 - distances[0][i], 2),
        }
        for i, idx in enumerate(indices[0])
    ]
    return recommendations