from fastapi import APIRouter, HTTPException
from models import Ingredient, Recipe, RecipeResult
from db import ingredients_db, recipes_db
from utils import calculate_recipe

router = APIRouter()

# Ingredients
@router.post("/ingredients", response_model=Ingredient)
def add_ingredient(ingredient: Ingredient):
    if ingredient.id in ingredients_db:
        raise HTTPException(status_code=400, detail="Ingredient ID already exists")
    ingredients_db[ingredient.id] = ingredient
    return ingredient

@router.get("/ingredients/{ingredient_id}", response_model=Ingredient)
def get_ingredient(ingredient_id: int):
    ingredient = ingredients_db.get(ingredient_id)
    if not ingredient:
        raise HTTPException(status_code=404, detail="Ingredient not found")
    return ingredient

@router.get("/ingredients", response_model=list[Ingredient])
def get_all_ingredients():
    return list(ingredients_db.values())

@router.delete("/ingredients/{ingredient_id}")
def delete_ingredient(ingredient_id: int):
    if ingredient_id not in ingredients_db:
        raise HTTPException(status_code=404, detail="Ingredient not found")
    del ingredients_db[ingredient_id]
    return {"message": f"Ingredient {ingredient_id} deleted successfully"}

# Recipes
@router.post("/recipes", response_model=Recipe)
def add_recipe(recipe: Recipe):
    if recipe.id in recipes_db:
        raise HTTPException(status_code=400, detail="Recipe ID already exists")
    recipes_db[recipe.id] = recipe
    return recipe

@router.get("/recipes/{recipe_id}", response_model=RecipeResult)
def get_recipe(recipe_id: int):
    recipe = recipes_db.get(recipe_id)
    if not recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return calculate_recipe(recipe)

@router.get("/recipes", response_model=list[Recipe])
def get_all_recipes():
    return list(recipes_db.values())

@router.delete("/recipes/{recipe_id}")
def delete_recipe(recipe_id: int):
    if recipe_id not in recipes_db:
        raise HTTPException(status_code=404, detail="Recipe not found")
    del recipes_db[recipe_id]
    return {"message": f"Recipe {recipe_id} deleted successfully"}
