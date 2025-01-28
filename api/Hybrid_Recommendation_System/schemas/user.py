from pydantic import BaseModel
from typing import List, Dict

class AttractionTagScore(BaseModel):
    attractionTagFields: Dict[str, float]

class UserInput(BaseModel):
    _id: str
    attractionTagScore: AttractionTagScore