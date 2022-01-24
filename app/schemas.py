from typing import List, Optional
from pydantic import BaseModel
from .db.models import Order
from pydantic_sqlalchemy import sqlalchemy_to_pydantic


class OrderItemCreate(BaseModel):
	menu_id: int
	category_id: int
	unit_price: float
	quantity: int


class OrderItem(OrderItemCreate):
	id: int
	order_id: int

	class Config:
		orm_mode = True


class MenuItemCreate(BaseModel):
	name: str


class MenuItem(MenuItemCreate):
	id: int
	order_items: List[OrderItem] = []

	class Config:
		orm_mode = True


class CategoryCreate(BaseModel):
	name: str


class Category(CategoryCreate):
	id: int
	order_items: List[OrderItem] = []

	class Config:
		orm_mode = True


class OrderBase(BaseModel):
	restaurant_id: int
	customer_id: int
	address_id: int
	confirmed_at: Optional[str] = None


class OrderCreate(OrderBase):
	order_items: List[OrderItemCreate]


# `sqlalchemy_to_pydantic()`
# https://github.com/tiangolo/pydantic-sqlalchemy
# Has the attribute `from_orm()` that converts an ORM object to a Pydantic Model (required in the project)
# Doesn't require the fields definition, only thre relational fields (check the class below)
PydanticOrder = sqlalchemy_to_pydantic(Order) 


class Order(OrderBase):
	id: int
	order_items: List[OrderItem] = []

	class Config:
		orm_mode = True
