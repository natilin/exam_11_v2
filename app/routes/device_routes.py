from flask import Blueprint, jsonify, request

from app.repositories.device_repository import get_device_bluetooth_connected_path, get_strong_signal_connected_path, \
    get_num_of_connected_to_device, check_if_connected, get_most_recent_interaction

device_blueprint = Blueprint("device", __name__)

@device_blueprint.route("/bluetooth", methods=["GET"])
def get_longest_connection():
    try:
        res = get_device_bluetooth_connected_path()
        return jsonify(res.value_or({})), 200
    except Exception as e:
        return str(e), 400


@device_blueprint.route("/strong", methods=["GET"])
def get_strong_connection():
    try:
        res = get_strong_signal_connected_path()
        return jsonify(res.value_or({})), 200
    except Exception as e:
        return str(e), 400


@device_blueprint.route("/count/<device_id>/", methods=["GET"])
def get_count_connection(device_id):
    try:
        res = get_num_of_connected_to_device(device_id)
        return jsonify(res.value_or({})), 200
    except Exception as e:
        return str(e), 400


@device_blueprint.route("/check-connection", methods=["POST"])
def check_connection():
    try:
        device_1 = request.json["device_1"]
        device_2 = request.json["device_2"]
        res = check_if_connected(device_1, device_2)
        return jsonify(res), 200
    except Exception as e:
        return str(e), 400


@device_blueprint.route("/recent-interaction/<device_id>", methods=["GET"])
def recent_connection(device_id):
    try:
        res = get_most_recent_interaction(device_id)
        return jsonify(res.value_or({})), 200
    except Exception as e:
        return str(e), 400


