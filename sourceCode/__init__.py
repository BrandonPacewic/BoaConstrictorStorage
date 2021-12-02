from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DB_name = 'database.db'

def create_boa():
    boa = Flask(__name__)
    boa.config['SECRET_KEY'] = 'ihaveboainmyroom'
    boa.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_name}'
    db.init_app(boa)

    from .views import views
    from .auth import auth

    boa.register_blueprint(views, url_prefix = '/')
    boa.register_blueprint(auth, url_prefix = '/')

    return boa
