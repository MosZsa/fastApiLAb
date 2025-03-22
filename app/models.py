from pydantic import BaseModel
from typing import List

class Ingredient(BaseModel):
    id: int
    name: str
    calories: float
    protein: float
    fat: float
    carbs: float

class RecipeIngredient(BaseModel):
    ingredient_id: int
    quantity: float

class Recipe(BaseModel):
    id: int
    name: str
    ingredients: List[RecipeIngredient]

class RecipeResult(BaseModel):
    name: str
    total_weight: float
    total_calories: float
    total_protein: float
    total_fat: float
    total_carbs: float