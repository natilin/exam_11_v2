from app.db.database import driver


def get_device_connected_path():
    with driver.session() as session:
        query = """
        match path=((d:Device) -[:CONNECTED{method:"Bluetooth"}]->(:Device))
        return path
        """
        return session.run(query).data()