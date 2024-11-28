from app.db.models import Device


def device_json_to_model(json: dict):
    json.update(json.pop("location"))
    return Device(**json)