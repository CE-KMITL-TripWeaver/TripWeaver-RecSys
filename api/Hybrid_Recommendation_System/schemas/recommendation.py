from pydantic import BaseModel
from typing import List, Dict

class RecommendationResponse(BaseModel):
    res_recommendation: List[str]