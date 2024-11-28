from app.db.database import driver
from app.db.models import Device, Interaction


def create_interaction(device1: Device, device2: Device, interaction: Interaction):
    with driver.session() as session:
        query = """
        merge(d1{id: $id, brand: $brand, model: $model, os: $os, latitude: $latitude, longitude: $longitude, altitude_meters: $altitude_meters, accuracy_meters: $accuracy_meters})
        """