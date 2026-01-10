from flask import Flask
import pymysql
import os
from dotenv import load_dotenv

load_dotenv()


def create_app():
    app = Flask(__name__)

    # Register the routes
    from .routes import main

    app.register_blueprint(main)

    return app


def get_db_connection():
    return pymysql.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
    )
