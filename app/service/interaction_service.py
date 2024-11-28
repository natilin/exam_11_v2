from app.db.models import Interaction
from app.repositories.interaction_repository import create_interaction
from app.service.device_service import device_json_to_model


def create_new_interaction(data: dict):
    device1 = device_json_to_model(data["devices"][0])
    device2 = device_json_to_model(data["devices"][1])
    interaction = Interaction(**data["interaction"])

    res = create_interaction(device1, device2, interaction)
    return res









def is_self_call(data:dict):
    pass

