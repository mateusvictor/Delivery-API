from .db.database import SessionLocal


def get_db():
	db = SessionLocal()
	try:
		yield db
	finally:
		db.close()

def calculate_relevance(order: dict):
	order_items = order.pop('order_items')
	items_quantity = 0

	menu_ids = set()
	menu_prices = {}
	menu_quantity = {}

	for order_item in order_items:
		menu_ids.add(order_items['menu_id'])

		menu_quantity = {''}
		items_quantity += order_items['quantity']

