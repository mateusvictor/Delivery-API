from sqlalchemy.orm import Session
from .db.models import *
from . import schemas


def init_db(db: Session):
	models = [Restaurant, Address, Customer, MenuItem]
	obj_per_model = 2
	for model in obj_per_model*models:
		db.add(model())

	db_category = Category(name='PIZZA')
	db.add(db_category)
	db_category = Category(name='SOUP')
	db.add(db_category)
	db_category = Category(name='LASAGNA')
	db.add(db_category)

	db.commit()


def create_category(db: Session, category: schemas.CategoryCreate):
	db_category = Category(**category.dict())
	db.add(db_category)
	db.commit()
	db.refresh(db_category)
	return db_category


def read_categories(db: Session):
	return db.query(Category).all()


def create_order_item(db: Session, order_id: int, order_item: dict):
	db_order_item = OrderItem(**order_item)
	db.add(db_order_item)


def create_order(db: Session, order: schemas.OrderCreate):
	order_dict = order.dict()
	order_items = order_dict.pop('order_items')
	
	order = Order(**order_dict)
	db.add(order)
	db.commit()
	db.refresh(order)

	for item in order_items:
		db_order_item = OrderItem(order_id=order.id, **item)
		db.add(db_order_item)

	db.commit()
	return order


def read_orders(db: Session):
	db_orders = db.query(Order).all()
	return db_orders


def read_order_by_id(db: Session, order_id: int):
	db_order = db.query(Order).filter(Order.id == order_id).first()
	return db_order

