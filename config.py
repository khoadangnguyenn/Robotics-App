import os
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv("API_KEY")
DATABASE_URL = os.getenv("DATABASE_URL")
SECRET_KEY = os.getenv("SECRET_KEY")
DEBUG = True

class Config:
    @staticmethod
    def _init_app__(app):
        app.config['API_KEY'] = API_KEY
        app.config['DATABASE_URL'] = DATABASE_URL
        app.config['SECRET_KEY'] = SECRET_KEY
        app.config['DEBUG'] = DEBUG