from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from FinalProject.api.models import sandwiches
from ..models import models, schemas


def create_sandwich(db: Session, sandwich):
    return sandwich.create(db)

def read_sandwiches(db: Session):
    return sandwiches.read_all(db)


def read_one_sandwich(db: Session, sandwich_id):
    return sandwich_id.read_one(db)


def update(db: Session, sandwich_id, data):
    return sandwich_id.update(db, sandwich_id, data)

def delete_sandwich(db: Session, sandwich_id):
    return sandwich_id.delete(db)

def read_all_sandwiches(db: Session):
    return db.query(sandwiches.Sandwich).all()

def read_one_sandwiche(db: Session, sandwich_id):
    return db.query(sandwiches.Sandwich).get(sandwich_id)
