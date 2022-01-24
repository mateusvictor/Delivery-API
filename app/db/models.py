from sqlalchemy import Boolean, Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base


# Database schema (V1): https://github.com/mateusvictor/Delivery-API/blob/main/screenshots/db-schema-v1.png
# '<-': This table is referenced by:
# '->': This table references:

class Restaurant(Base):
	__tablename__ = 'restaurants'
	id = Column(Integer, primary_key=True, index=True)
	# <-
	orders = relationship('Order', back_populates='restaurant')


class Address(Base):
	__tablename__ = 'addresses'
	id = Column(Integer, primary_key=True, index=True)
	# <-
	orders = relationship('Order', back_populates='address')
	

class Customer(Base):
	__tablename__ = 'customers'
	id = Column(Integer, primary_key=True, index=True)
	# <-
	orders = relationship('Order', back_populates='customer')
	

class Category(Base):
	__tablename__ = 'categories'
	id = Column(Integer, primary_key=True, index=True)
	name = Column(String, index=True, unique=True)
	# <-
	order_items = relationship('OrderItem', back_populates='category')


class MenuItem(Base):
	__tablename__ = 'menu_items'
	id = Column(Integer, primary_key=True, index=True)
	# name = Column(String, index=True)
	# description = Column(String, index=True)
	# <-
	order_items = relationship('OrderItem', back_populates='menu_item')


class Order(Base):
	__tablename__ = 'orders'
	id = Column(Integer, primary_key=True, index=True)
	restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
	customer_id = Column(Integer, ForeignKey('customers.id'))
	address_id = Column(Integer, ForeignKey('addresses.id'))
	confirmed_at = Column(String, index=True)
	# ->
	restaurant = relationship('Restaurant', back_populates='orders')
	customer = relationship('Customer', back_populates='orders')
	address = relationship('Address', back_populates='orders')
	# <-
	order_items = relationship('OrderItem', back_populates='order')


class OrderItem(Base): 
	__tablename__ = 'order_items'
	id = Column(Integer, primary_key=True, index=True)
	order_id = Column(Integer, ForeignKey('orders.id'))
	menu_id = Column(Integer, ForeignKey('menu_items.id'))
	category_id = Column(Integer, ForeignKey('categories.id'))
	unit_price = Column(Float, index=True)	
	quantity = Column(Integer, index=True)
	# ->
	order = relationship('Order', back_populates='order_items')
	menu_item = relationship('MenuItem', back_populates='order_items')
	category = relationship('Category', back_populates='order_items')