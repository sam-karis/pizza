
import os
from app import create_app
from app import db

app = create_app(os.getenv("APP_SETTINGS", default="config.DevelopmentConfig"))

from models.pizza import SizeReference, Pizza, ToppingType, ToppingTypeSize, ToppingReference, Topping


@app.before_first_request
def before_first_request_func():
    # This function will run once
    db.session.add(SizeReference(name='Large'))
    db.session.add(SizeReference(name='Medium'))
    db.session.add(SizeReference(name='Small'))
    db.session.add(ToppingType(name='Basic Toppings'))
    db.session.add(ToppingType(name='Deluxe Toppings'))
    db.session.add(ToppingReference(name='Cheese'))
    db.session.add(ToppingReference(name='Pepperoni'))
    db.session.add(ToppingReference(name='Ham'))
    db.session.add(ToppingReference(name='Pineapple'))
    db.session.add(ToppingReference(name='Sausage'))
    db.session.add(ToppingReference(name='Feta Cheese'))
    db.session.add(ToppingReference(name='Tomatoes'))
    db.session.add(ToppingReference(name='Olives'))
    db.session.add(Pizza(size_id=1, price=1600))
    db.session.add(Pizza(size_id=2, price=1400))
    db.session.add(Pizza(size_id=3, price=1200))
    db.session.add(ToppingTypeSize(topping_type_id=1, size_id=1, price=100))
    db.session.add(ToppingTypeSize(topping_type_id=1, size_id=2, price=75))
    db.session.add(ToppingTypeSize(topping_type_id=1, size_id=3, price=50))
    db.session.add(ToppingTypeSize(topping_type_id=2, size_id=1, price=400))
    db.session.add(ToppingTypeSize(topping_type_id=2, size_id=2, price=300))
    db.session.add(ToppingTypeSize(topping_type_id=2, size_id=3, price=200))
    db.session.add(Topping(topping_type_size_id=1, topping_ref_id=1))
    db.session.add(Topping(topping_type_size_id=2, topping_ref_id=1))
    db.session.add(Topping(topping_type_size_id=3, topping_ref_id=1))
    db.session.add(Topping(topping_type_size_id=1, topping_ref_id=2))
    db.session.add(Topping(topping_type_size_id=2, topping_ref_id=2))
    db.session.add(Topping(topping_type_size_id=3, topping_ref_id=2))
    db.session.add(Topping(topping_type_size_id=1, topping_ref_id=3))
    db.session.add(Topping(topping_type_size_id=2, topping_ref_id=3))
    db.session.add(Topping(topping_type_size_id=3, topping_ref_id=3))
    db.session.add(Topping(topping_type_size_id=1, topping_ref_id=4))
    db.session.add(Topping(topping_type_size_id=2, topping_ref_id=4))
    db.session.add(Topping(topping_type_size_id=3, topping_ref_id=4))
    db.session.add(Topping(topping_type_size_id=4, topping_ref_id=5))
    db.session.add(Topping(topping_type_size_id=5, topping_ref_id=5))
    db.session.add(Topping(topping_type_size_id=6, topping_ref_id=5))
    db.session.add(Topping(topping_type_size_id=4, topping_ref_id=6))
    db.session.add(Topping(topping_type_size_id=5, topping_ref_id=6))
    db.session.add(Topping(topping_type_size_id=6, topping_ref_id=6))
    db.session.add(Topping(topping_type_size_id=4, topping_ref_id=7))
    db.session.add(Topping(topping_type_size_id=5, topping_ref_id=7))
    db.session.add(Topping(topping_type_size_id=6, topping_ref_id=7))
    db.session.add(Topping(topping_type_size_id=4, topping_ref_id=8))
    db.session.add(Topping(topping_type_size_id=5, topping_ref_id=8))
    db.session.add(Topping(topping_type_size_id=6, topping_ref_id=8))
    db.session.commit()
