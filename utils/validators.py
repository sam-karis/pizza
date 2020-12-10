from functools import wraps

from flask import request


def validate_order(func):
    """
    It's a decorator that validate that the data is of right format
    :param func:
    :return:
        error : error message and appropriate status code
        success: allow execution of the request
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        if request.mimetype != "text/plain":
            return {"error": "Invalid request"}, 400
        data = request.data.decode('utf-8').split("\n")
        res = {}
        available_pizza = ("Large", "Medium", "Small")
        available_topping = ("Cheese", "Pepperoni", "Ham", "Pineapple",
                             "Sausage", "Feta Cheese", "Tomatoes", "Olives")
        for pizza in data:
            pizza_list = pizza.split("-")
            pizza_name = pizza_list[0].strip(" ").capitalize()
            if pizza_name not in available_pizza:
                if "invalidPizza" not in res:
                    res["invalidPizza"] = []
                    res["invalidPizza"].append(pizza_name)
                else:
                    res["invalidPizza"].append(pizza_name)
            topping_list = pizza_list[-1].split(",")
            topping_list = list(filter(lambda x: x != "", topping_list))
            for topping in topping_list:
                topping = topping.strip(" ").capitalize()
                if topping not in available_topping:
                    if "invalidTopping" not in res:
                        res["invalidTopping"] = []
                        res["invalidTopping"].append(topping)
                    else:
                        res["invalidTopping"].append(topping)

            if res:
                return {
                           "message": "Invalid request",
                           "errors": res

                       }, 400

        return func(*args, **kwargs)

    return wrapper
