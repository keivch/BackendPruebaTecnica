from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    CORS(app)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../instance/app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}})

    from .routes import book_bp
    app.register_blueprint(book_bp)

    with app.app_context():
        db.create_all()

    return app
