-- Database schema (V1): https://github.com/mateusvictor/Delivery-API/blob/main/screenshots/db-schema-v1.png


CREATE TABLE restaurants (
	id SERIAL NOT NULL, 
	PRIMARY KEY (id)
);
CREATE INDEX ix_restaurants_id ON restaurants (id);


CREATE TABLE addresses (
	id SERIAL NOT NULL, 
	PRIMARY KEY (id)
);
CREATE INDEX ix_addresses_id ON addresses (id);


CREATE TABLE customers (
	id SERIAL NOT NULL, 
	PRIMARY KEY (id)
);
CREATE INDEX ix_customers_id ON customers (id);


CREATE TABLE categories (
	id SERIAL NOT NULL, 
	name VARCHAR, 
	PRIMARY KEY (id)
);
CREATE INDEX ix_categories_id ON categories (id);
CREATE UNIQUE INDEX ix_categories_name ON categories (name);


CREATE TABLE menu_items (
	id SERIAL NOT NULL, 
	PRIMARY KEY (id)
);
CREATE INDEX ix_menu_items_id ON menu_items (id);


CREATE TABLE orders (
	id SERIAL NOT NULL, 
	restaurant_id INTEGER, 
	customer_id INTEGER, 
	address_id INTEGER, 
	confirmed_at VARCHAR, 
	PRIMARY KEY (id), 
	FOREIGN KEY(restaurant_id) REFERENCES restaurants (id), 
	FOREIGN KEY(customer_id) REFERENCES customers (id), 
	FOREIGN KEY(address_id) REFERENCES addresses (id)
);
CREATE INDEX ix_orders_confirmed_at ON orders (confirmed_at);
CREATE INDEX ix_orders_id ON orders (id);


CREATE TABLE order_items (
	id SERIAL NOT NULL, 
	order_id INTEGER, 
	menu_id INTEGER, 
	category_id INTEGER, 
	unit_price FLOAT, 
	quantity INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(order_id) REFERENCES orders (id), 
	FOREIGN KEY(menu_id) REFERENCES menu_items (id), 
	FOREIGN KEY(category_id) REFERENCES categories (id)
);
CREATE INDEX ix_order_items_unit_price ON order_items (unit_price);
CREATE INDEX ix_order_items_quantity ON order_items (quantity);
CREATE INDEX ix_order_items_id ON order_items (id);