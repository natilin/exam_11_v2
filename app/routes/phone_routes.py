from flask import Blueprint, request, jsonify

from app.service.interaction_service import create_new_interaction

phone_blueprint = Blueprint("phone", __name__)

@phone_blueprint.route("/", methods=['POST'])
def get_interaction():
   data = request.json
   print(data)
   res = create_new_interaction(data)
   return jsonify({}), 200