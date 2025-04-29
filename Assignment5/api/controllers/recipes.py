from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from FinalProject.api.models import recipes
from ..models import models, schemas

def read_all_recipes(db: Session):
    return db.query(models.Recipe).all()

def read_one_recipe(db: Session, recipe_id: int):
    return db.query(models.Recipe).filter(models.Recipe.id == recipe_id).first()

def create_recipes(db: Session, recipe: schemas.recipes):
    return create_recipes(db, recipe)

def read_recipes(db: Session, recipe_id: int):
    return read_recipes(db, recipe_id)

def update_recipes(db: Session, recipe_id: int, recipe: schemas.recipes):
    return update_recipes(db, recipe_id, recipe)

def delete_recipes(db: Session, recipe_id: int):
    return delete_recipes(db, recipe_id)

def get_recipes(db: Session, recipe_id: int):
    return get_recipes(db, recipe_id)



