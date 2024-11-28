from flask import Blueprint

device_blueprint = Blueprint("device", __name__)

@device_blueprint.route("/connection", methods=["GET"])
def get_all_connection():
