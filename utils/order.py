from app import db
from models.order import Order, UserRequest, Receipt
from models.pizza import Topping, Pizza, SizeReference, ToppingReference, ToppingTypeSize


def record_order(order_data):
    """
    This methods pick the data from the user request and save it into the database
    :param order_data:
    :return: receipt for the order saved
    """
    new_order = Order()
    pizza_query = db.session.query(Pizza).join(SizeReference)
    topping_query = db.session.query(Topping).join(ToppingReference).join(ToppingTypeSize).join(SizeReference)
    for unique_request in order_data:
        request_list = unique_request.split("-")
        pizza_size = request_list[0].strip(" ").capitalize()
        pizza_obj = pizza_query.filter(SizeReference.name == pizza_size).first()
        new_user_request = UserRequest(pizza_id=pizza_obj.id)
        topping_list = request_list[-1].split(",") if len(request_list) > 1 else []
        topping_list = list(filter(lambda x: x != "", topping_list))
        for topping in topping_list:
            topping_name = topping.strip(" ").capitalize()
            topping_obj = topping_query.filter(ToppingReference.name == topping_name).filter(
                SizeReference.name == pizza_size).first()
            new_user_request.toppings.append(topping_obj)
        new_order.user_requests.append(new_user_request)
    db.session.add(new_order)
    db.session.commit()
    new_receipt = Receipt(order_id=new_order.id)
    db.session.add(new_receipt)
    db.session.commit()
    return new_receipt
