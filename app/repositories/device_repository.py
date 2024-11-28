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
        RETURN path
        """
        return Maybe.from_optional(session.run(query).data())


def get_strong_signal_connected_path(min_strength=-30) -> Maybe:
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
        RETURN path
        """
        params = {"min_strength": min_strength}
        return Maybe.from_optional(session.run(query, params).data())

