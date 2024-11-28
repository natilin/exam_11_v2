from dataclasses import asdict

from app.db.database import driver
from app.db.models import Device, Interaction


def create_interaction(device1: Device, device2: Device, interaction: Interaction):
    with driver.session() as session:
        interaction = asdict(interaction)
        device1 = asdict(device1)
        device2 =  asdict(device2)

        # change the name of the device2 keys
        new_device2 = {key + "2": value for key, value in device2.items()}

        query = """
        merge(d1{device_id: $device_id,
            brand: $brand,
            model: $model,
            os: $os,
            latitude: $latitude,
            longitude: $longitude, 
            altitude_meters: $altitude_meters, 
            accuracy_meters: $accuracy_meters
        })
        merge(d2{device_id2: $device_id,
            brand: $brand2,
            model: $model2,
            os: $os2,
            latitude: $latitude2,
            longitude: $longitude2, 
            altitude_meters: $altitude_meters2, 
            accuracy_meters: $accuracy_meters2
        })
        create (d1) -[r:CONNECTED{method: $method, 
            bluetooth_version: $bluetooth_version, 
            signal_strength_dbm: $signal_strength_dbm, 
            distance_meters: $distance_meters, 
            duration_seconds: $duration_seconds, 
            timestamp: $timestamp}] -> (d2)
            return d1, r, d2
        """
        params = {**interaction, **device1, **new_device2}
        res = session.run(query, params).data()
        return res
