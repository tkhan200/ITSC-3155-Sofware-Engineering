from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from FinalProject.api.models import sandwiches
from ..models import models, schemas


def create_order_details(db: Session, order_detail: schemas.OrderDetailsCreate):
    return order_detail.save(db)

def read_order_details(db: Session, order_detail: schemas.OrderDetailsRead):
    return order_detail.load(db)

def read_one_order_details(db: Session, order_detail: schemas.OrderDetailsRead):
    return order_detail.load(db)

def update_order_details(db: Session, order_detail: schemas.OrderDetailsUpdate):
    return order_detail.update(db)

def delete_order_details(db: Session, order_detail: schemas.OrderDetailsDelete):
    return order_detail.delete(db)

def get_order_details(db: Session, order_detail: schemas.OrderDetailsGet):
    return order_detail.load(db)
