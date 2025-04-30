from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from .models import models, schemas
from .controllers import orders, sandwiches, order_details
from .dependencies.database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/orders/", response_model=schemas.Order, tags=["Orders"])
def create_order(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    return orders.create(db=db, order=order)


@app.get("/orders/", response_model=list[schemas.Order], tags=["Orders"])
def read_orders(db: Session = Depends(get_db)):
    return orders.read_all(db)


@app.get("/orders/{order_id}", response_model=schemas.Order, tags=["Orders"])
def read_one_order(order_id: int, db: Session = Depends(get_db)):
    order = orders.read_one(db, order_id=order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="User not found")
    return order


@app.put("/orders/{order_id}", response_model=schemas.Order, tags=["Orders"])
def update_one_order(order_id: int, order: schemas.OrderUpdate, db: Session = Depends(get_db)):
    order_db = orders.read_one(db, order_id=order_id)
    if order_db is None:
        raise HTTPException(status_code=404, detail="User not found")
    return orders.update(db=db, order=order, order_id=order_id)


@app.delete("/orders/{order_id}", tags=["Orders"])
def delete_one_order(order_id: int, db: Session = Depends(get_db)):
    order = orders.read_one(db, order_id=order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="User not found")
    return orders.delete(db=db, order_id=order_id)

@app.post("/recipes/", response_model=schemas.Recipe, tags=["Recipes"])
def create_recipes(recipes: schemas.OrderCreate, db: Session = Depends(get_db)):
    return orders.create(db=db, order=recipes)

@app.get("/recipes/", response_model=list[schemas.Recipe], tags=["Recipes"])
def read_recipes(db: Session = Depends(get_db)):
    return orders.read_all(db)

@app.get("/recipes/", response_model=list[schemas.Recipe], tags=["Recipes"])
def read_one_recipes(db: Session = Depends(get_db)):
    return orders.read_all(db)

@app.put("/recipes/", response_model=schemas.Recipe, tags=["Recipes"])
def update_recipes(db: Session, recipe_id: int, recipe: schemas.Recipe()):
    return update_recipes(db, recipe_id, recipe)

@app.delete("/recipes/", tags=["Recipes"])
def delete_recipes(db: Session = Depends(get_db)):
    return delete_recipes(db)

@app.post("/resources/", response_model=schemas.Resource, tags=["Resources"])
def create_recipes(db: Session, recipe: schemas.recipes):
    return create_recipes(db, recipe)

@app.get("/resources", response_model=list[schemas.Resource], tags=["Resources"])
def read_resources(db: Session = Depends(get_db)):
    return orders.read_all(db)

@app.get("/resources", response_model=list[schemas.Resource], tags=["Resources"])
def read_one_resources(db: Session = Depends(get_db)):
    return orders.read_all(db)

@app.put("/resources/", response_model=schemas.Resource, tags=["Resources"])
def update_resources(db: Session = Depends(get_db)):
    return update_resources(db)

@app.delete("/resources/", tags=["Resources"])
def delete_resources(db: Session = Depends(get_db)):
    return delete_resources(db)


@app.post("/sandwiches/", response_model=schemas.Sandwich, tags=["Sandwiches"])
def create_sandwich(db: Session, sandwich):
    return sandwich.create(db)

@app.get("/sandwiches/", response_model=schemas.Sandwich, tags=["Sandwiches"])
def read_sandwiches(db: Session = Depends(get_db)):
    return sandwiches.read_all(db)

@app.get("/sandwiches/", response_model=schemas.Sandwich, tags=["Sandwiches"])
def read_onr_sandwiches(db: Session = Depends(get_db)):
    return sandwiches.read_all(db)

@app.put("/sandwiches/", response_model=schemas.Sandwich, tags=["Sandwiches"])
def update_sandwiches(db: Session = Depends(get_db)):
    return update_sandwiches(db)

@app.delete("/sandwiches/", tags=["Sandwiches"])
def delete_sandwiches(db: Session = Depends(get_db)):
    return delete_sandwiches(db)

@app.post("/order_details/{order_id}", response_model=schemas.Order, tags=["Orders"])
def create_order_details(db: Session, order_detail: schemas.OrderDetailsCreate):
    return order_detail.save(db)

@app.get("/order_details/", response_model=schemas.Order, tags=["Orders"])
def read_order_details(db: Session = Depends(get_db)):
    return order_details.read(db)

@app.get("/orders/{order_id}", response_model=schemas.Order, tags=["Orders"])
def read_one_order(order_id: int, db: Session = Depends(get_db)):
    order = orders.read_one(db, order_id=order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="User not found")
    return order

@app.put("/orders/{order_id}", response_model=schemas.Order, tags=["Orders"])
def update_order_details(db: Session, order_detail: schemas.OrderDetailsUpdate):
    return order_detail.update(db)

@app.delete("/orders/{order_id}", tags=["Orders"])
def delete_order(order_id: int, db: Session = Depends(get_db)):
    order = orders.read_one(db, order_id=order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="User not found")
    return orders.delete(db=db, order=order_id)


