from flask import Flask

from app.routes.device_routes import device_blueprint
from app.routes.phone_routes import phone_blueprint

app = Flask(__name__)
app.register_blueprint(phone_blueprint, url_prefix="/api/phone_tracker")
app.register_blueprint(device_blueprint, url_prefix="/api/device")

if __name__ == "__main__":
    app.run()
