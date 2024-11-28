from dataclasses import dataclass, asdict


@dataclass
class Device:
    device_id: str
    brand: str
    model: str
    os: str
    latitude: int
    longitude: int
    altitude_meters: int
    accuracy_meters: int
