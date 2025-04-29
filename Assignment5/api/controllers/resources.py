from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from FinalProject.api.models import resources
from ..models import models, schemas

def read_all_resources(db: Session):
    return db.query(resources.Resource).all()

def read_one_resource(db: Session, id: int):
    return db.query(resources.Resource).filter(resources.Resource.id == id).first()


def create_resources(db: Session, resources: schemas.Resources):
    return resources.create(db)

def read_resources(db: Session, resources: schemas.Resources):
    return resources.read(db)

def update_resources(db: Session, resources: schemas.Resources):
    return resources.update(db)

def delete_resources(db: Session, resources: schemas.Resources):
    return resources.delete(db)

def get_resources(db: Session, resources: schemas.Resources):
    return resources.get(db)

