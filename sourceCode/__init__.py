from flask import Flask

def create_boa():
    boa = Flask(__name__)
    boa.config['SECRET_KEY'] = 'ihaveboainmyroom'

    from .views import views
    from .auth import auth

    boa.register_blueprint(views, url_prefix = '/')
    boa.register_blueprint(auth, url_prefix = '/')

    return boa
