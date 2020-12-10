from app import db
from models.base import BaseModel


class SizeReference(BaseModel, db.Model):
    __tablename__ = "size_reference"

    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String(80))
    pizzas = db.relationship(
        "Pizza", backref="size_ref", lazy=True, uselist=False
    )
    toppings_type_size = db.relationship(
        "ToppingTypeSize", backref="size_ref", lazy=True, uselist=False
    )

class Pizza(BaseModel, db.Model):
    __tablename__ = "pizza"

    id = db.Column(db.BigInteger, primary_key=True)
    price = db.Column(db.Integer)
    size_id = db.Column(
        db.Integer, db.ForeignKey("size_reference.id"), nullable=False
    )

    @property
    def size(self):
        return self.size_ref.name


class ToppingType(BaseModel, db.Model):
    __tablename__ = "topping_type"

    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String(80))
    toppings_type_size = db.relationship(
        "ToppingTypeSize", backref="topping_type", lazy=True, uselist=False
    )


class ToppingTypeSize(BaseModel, db.Model):
    __tablename__ = "topping_type_size"

    id = db.Column(db.BigInteger, primary_key=True)
    price = db.Column(db.Integer)
    size_id = db.Column(
        db.Integer, db.ForeignKey("size_reference.id"), nullable=False
    )
    topping_type_id = db.Column(
        db.Integer, db.ForeignKey("topping_type.id"), nullable=False
    )
    toppings = db.relationship(
        "Topping", backref="topping_type_size", lazy=True, uselist=False
    )

    @property
    def topping_type(self):
        return self.topping_type.name

    @property
    def size(self):
        return self.size_ref.name


class ToppingReference(BaseModel, db.Model):
    __tablename__ = "topping_reference"

    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String(80))
    toppings = db.relationship(
        "Topping", backref="topping_ref", lazy=True, uselist=False
    )


class Topping(BaseModel, db.Model):
    __tablename__ = "topping"

    id = db.Column(db.BigInteger, primary_key=True)
    topping_ref_id = db.Column(
        db.Integer, db.ForeignKey("topping_reference.id"), nullable=False
    )
    topping_type_size_id = db.Column(
        db.Integer, db.ForeignKey("topping_type_size.id"), nullable=False
    )

    @property
    def price(self):
        return self.topping_type_size.price

    @property
    def name(self):
        return self.topping_ref.name
