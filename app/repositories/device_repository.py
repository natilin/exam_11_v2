from returns.maybe import Maybe

from app.db.database import driver


def get_device_bluetooth_connected_path() -> Maybe:
    with driver.session() as session:
        query = """
        MATCH (start:Device)
        MATCH (end:Device)
        WHERE start <> end
        MATCH path = shortestPath((start)-[:CONNECTED*]->(end))
        WHERE ALL(r IN relationships(path) WHERE r.method = 'Bluetooth')
        WITH path, length(path) as pathLength
        ORDER BY pathLength DESC
        LIMIT 1
        RETURN path, pathLength
        """
        return Maybe.from_optional(session.run(query).data())


def get_strong_signal_connected_path(min_strength=-60) -> Maybe:
    with driver.session() as session:
        query = """
        MATCH (start:Device)
        MATCH (end:Device)
        WHERE start <> end
        MATCH path = shortestPath((start)-[:CONNECTED*]->(end))
        WHERE ALL(r IN relationships(path) WHERE r.signal_strength_dbm >= $min_strength)
        WITH path, length(path) as pathLength
        ORDER BY pathLength DESC
        LIMIT 1
        RETURN path, pathLength
        """
        params = {"min_strength": min_strength}
        return Maybe.from_optional(session.run(query, params).data())


def get_num_of_connected_to_device(device_id: str):
    with driver.session() as session:
        query = """
            MATCH (d: Device{device_id: $device_id) <-[:CONNECTED] - (d2:Device) 
            return count(d2) as connected_devices
        """
        params = {"device_id": device_id}
        return  Maybe.from_optional(session.run(query, params).data())


def check_if_connected(device1_id: str, device2_id: str):
    with driver.session() as session:
        query = """
            MATCH (d: Device{device_id: $id1}) <-[r:CONNECTED] - (d2:Device{device_id: $id2}) 
            return d, r, d2
        """
        params = {"id1": device1_id, "id2": device2_id}
        res = session.run(query, params).data()
        if res:
            return res
        return {"massage": "no connection"}


def get_most_recent_interaction(device_id: str) -> Maybe:
        with driver.session() as session:
            query = """
                MATCH (d:Device {id: $device_id})-[rel:CONNECTED]->(d2:Device)
                RETURN d, rel, d2
                ORDER BY rel.timestamp DESC
                LIMIT 1
            """
            params = {"device_id": device_id}
            return  Maybe.from_optional(session.run(query, params).data())

