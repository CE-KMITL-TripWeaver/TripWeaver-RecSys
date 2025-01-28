from pydantic import BaseModel
from typing import List, Dict

class AttractionTagFields(BaseModel):
    Dict[str, float]

class AttractionTagScore(BaseModel):
    attractionTagFields: AttractionTagFields

class UserInput(BaseModel):
    _id: str
    attractionTagScore: AttractionTagScore