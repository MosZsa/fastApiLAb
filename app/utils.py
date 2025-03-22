from db import ingredients_db
from models import Recipe, RecipeResult
from fastapi import HTTPException

def calculate_recipe(recipe: Recipe) -> RecipeResult:
    total_weight = 0
    total_calories = 0
    total_protein = 0
    total_fat = 0
    total_carbs = 0

    for item in recipe.ingredients:
        ingredient = ingredients_db.get(item.ingredient_id)
        if not ingredient:
            raise HTTPException(status_code=404, detail=f"Ingredient ID {item.ingredient_id} not found")
        factor = item.quantity / 100
        total_weight += item.quantity
        total_calories += ingredient.calories * factor
        total_protein += ingredient.protein * factor
        total_fat += ingredient.fat * factor
        total_carbs += ingredient.carbs * factor

    return RecipeResult(
        name=recipe.name,
        total_weight=total_weight,
        total_calories=round(total_calories, 2),
        total_protein=round(total_protein, 2),
        total_fat=round(total_fat, 2),
        total_carbs=round(total_carbs, 2)
    )
