from pydantic import BaseModel
from typing import List, Dict

class AttractionTagFields(BaseModel):
    Tourism: float
    Adventure: float
    Meditation: float
    Art: float
    Cultural: float
    Landscape: float
    Nature: float
    Historical: float
    Cityscape: float
    Beach: float
    Mountain: float
    Architecture: float
    Temple: float
    WalkingStreet: float
    Market: float
    Village: float
    NationalPark: float
    Diving: float
    Snuggle: float
    Waterfall: float
    Island: float
    Shopping: float
    Camping: float
    Fog: float
    Cycling: float
    Monument: float
    Zoo: float
    Waterpark: float
    Hiking: float
    Museum: float
    Riverside: float
    NightLife: float
    Family: float
    Kid: float
    Landmark: float
    Forest: float

class AttractionTagScore(BaseModel):
    attractionTagFields: AttractionTagFields

class UserInput(BaseModel):
    _id: str
    attractionTagScore: AttractionTagScore