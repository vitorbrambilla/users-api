from flask import Flask
from flask_cors import CORS
from src.main.routes.users import users_route_bp
from src.models.settings.connection import db_connection_handler

db_connection_handler.connect_to_db()

app = Flask(__name__)
CORS(app)

app.register_blueprint(users_route_bp)
