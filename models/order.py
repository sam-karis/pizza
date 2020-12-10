from collections import Counter

from num2words import num2words

from app import db
from models.base import BaseModel

topping_combination = db.Table(
    "topping_request",
    db.Column(
        "user_request_id",
        db.Integer,
        db.ForeignKey("user_request.id"),
        primary_key=True,
    ),
    db.Column(
        "topping",
        db.Integer,
        db.ForeignKey("topping.id"),
        primary_key=True,
    ),
)


class UserRequest(BaseModel, db.Model):
    __tablename__ = "user_request"

    id = db.Column(db.BigInteger, primary_key=True)
    pizza_id = db.Column(
        db.Integer, db.ForeignKey("pizza.id"), nullable=False
    )
    toppings = db.relationship('Topping', secondary=topping_combination, lazy='subquery',
                               backref=db.backref('user_requests', lazy=True))

    @property
    def price(self):
        pizza_price = self.pizza.price
        topping_price = [topping.price for topping in self.toppings]
        return pizza_price + sum(topping_price)

    @property
    def pizza_size(self):
        return self.pizza.size

    @property
    def summary(self):
        topping_counter = Counter([topping.name for topping in self.toppings])
        topping_count = len(topping_counter)
        topping_summary = f"{num2words(topping_count).capitalize()} Topping Pizza"
        if topping_count >= 1:
            topping_summary += " - "
            count = 0
            for topping, count_ in topping_counter.items():
                if count_ > 1:
                    topping = f"{num2words(count_).capitalize()} {topping}"
                count += 1
                if topping_count - count == 1:
                    topping_summary += f"{topping} "
                elif count < topping_count:
                    topping_summary += f"{topping}, "
                else:
                    topping_summary += f"and {topping}"
        return f"{self.pizza_size}, {topping_summary}: KES {self.price}"


order_combination = db.Table(
    "order_requests",
    db.Column(
        "order_id",
        db.Integer,
        db.ForeignKey("order.id"),
        primary_key=True,
    ),
    db.Column(
        "user_request_id",
        db.Integer,
        db.ForeignKey("user_request.id"),
        primary_key=True,
    ),
)


class Order(BaseModel, db.Model):
    __tablename__ = "order"

    id = db.Column(db.BigInteger, primary_key=True)
    user_requests = db.relationship('UserRequest', secondary=order_combination, lazy='subquery',
                                    backref=db.backref('order', lazy=True))
    receipt = db.relationship(
        "Receipt", backref="order", lazy=True, uselist=False
    )

    @property
    def price_vat(self):
        subtotal = sum([user_request.price for user_request in self.user_requests])
        VAT = round((subtotal * 0.16))
        return subtotal, VAT


class Receipt(BaseModel, db.Model):
    __tablename__ = "receipt"

    id = db.Column(db.BigInteger, primary_key=True)
    order_id = db.Column(
        db.Integer, db.ForeignKey("order.id"), nullable=False
    )

    @property
    def order_details(self):
        user_req_list = [user_request.summary for user_request in self.order.user_requests]
        user_req_counter = Counter(user_req_list)
        subtotal, VAT = self.order.price_vat
        response = ""
        for user_request, count in user_req_counter.items():
            response += f"{count} {user_request}\n"
        response += f"\n\nSubtotal: KES {subtotal} \nVAT: KES {VAT}"

        return response
