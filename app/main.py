from datetime import datetime
from typing import List
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, schemas
from .db import models
from .db.database import engine
from .dependencies import get_db


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post('/init_db/', response_model=[], tags=['init'])
def init_db(db=Depends(get_db)):
	crud.init_db(db=db)
	return []

# ------------------------------------ Category Model ------------------------------------

@app.post('/categories/', response_model=schemas.Category, tags=['category'])
def create_category(category: schemas.CategoryCreate, db: Session = Depends(get_db)):
	db_category = crud.create_category(db=db, category=category)
	return db_category


@app.get('/categories/', response_model=List[schemas.Category], tags=['category'])
def read_categories(db: Session = Depends(get_db)):
	return crud.read_categories(db=db)

# ------------------------------------ Order Model ------------------------------------

@app.post('/orders/', response_model=schemas.Order, tags=['order'])
def create_order(order: schemas.OrderCreate, db: Session = Depends(get_db)):
	db_order = crud.create_order(db=db, order=order)
	return db_order


@app.get('/orders/', response_model=List[schemas.Order], tags=['order'])
def read_orders(db: Session = Depends(get_db)):
	return crud.read_orders(db=db)


@app.get('/orders/{order_id}/', response_model=schemas.Order, tags=['order'])
def read_order(order_id: int, db: Session = Depends(get_db)):
	db_order = crud.read_order_by_id(db=db, order_id=order_id)

	if db_order == None:
		raise HTTPException(status_code=404, detail='Invalid order ID')
	
	pydantic_order = schemas.Order.from_orm(db_order)
	print(pydantic_order.dict())
	return db_order
