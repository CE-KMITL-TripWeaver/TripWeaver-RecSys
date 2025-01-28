from pydantic import BaseModel
from typing import List, Dict

class Recommendation(BaseModel):
    id: str
    name: str
    sim_score: float

class RecommendationResponse(BaseModel):
    res_recommendation: List[Recommendation]