from flask import Blueprint, request

from utils.order import record_order
from utils.validators import validate_order

bp = Blueprint("order", __name__)


@bp.route("/make-order", methods=["POST"])
@validate_order
def make_order():
    """"
    Handles the logic for making an order and return receipt
    """
    data = request.data.decode('utf-8').split("\n")
    receipt = record_order(data)
    return receipt.order_details
