from flask import Blueprint, jsonify

from app.repositories.device_repository import get_device_bluetooth_connected_path, get_strong_signal_connected_path

device_blueprint = Blueprint("device", __name__)

@device_blueprint.route("/bluetooth-connection", methods=["GET"])
def get_longest_connection():
    res = get_device_bluetooth_connected_path()
    return jsonify(res.value_or({})), 200


@device_blueprint.route("/strong-connection", methods=["GET"])
def get_strong_connection():
    res = get_strong_signal_connected_path()
    return jsonify(res.value_or({})), 200