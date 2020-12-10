from flask import Blueprint

bp = Blueprint("index", __name__)


@bp.route("/", methods=["GET"])
def index():
    return {"message": "Welcome to pizza ordering system"}
