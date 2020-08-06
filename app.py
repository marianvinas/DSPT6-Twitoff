from flask import Flask
from .db_model import dbgit

def create_app():
    '''Create and configure an instance of the Flask application'''

    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///C:\\Users\\bruno\\Desktop\\DSPT6-Twitoff\\twitoff\\twitoff.sqlite"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    @app.route('/')
    def root():
        return 'Welcome to Twitoff!'

    return app