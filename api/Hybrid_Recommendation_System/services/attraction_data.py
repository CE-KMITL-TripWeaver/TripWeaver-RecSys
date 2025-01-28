import requests
from fastapi import HTTPException
from typing import List, Dict, Tuple

def fetch_attraction_data(api_endpoint: str) -> List[Dict]:
    try:
        response = requests.post(api_endpoint).json()
        if "attractions" not in response:
            raise ValueError("Invalid response from API")
        return response["attractions"]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch attraction data: {e}")

def preprocess_attraction_data(attractions: List[Dict]) -> Tuple[List[List[float]], List[tuple]]:
    attraction_data = []
    attraction_refs = []
    for attraction in attractions:
        tag_scores = attraction["attractionTag"]["attractionTagFields"]
        tag_scores = attraction["attractionTag"]["attractionTagFields"]
        attraction_data.append(list(tag_scores.values()))
        attraction_refs.append((attraction["_id"], attraction["name"]))
    return attraction_data, attraction_refs