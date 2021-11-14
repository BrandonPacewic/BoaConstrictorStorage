from flask import Flask

def create_boa():
    boa = Flask(__name__)
    boa.config['SECRET_KEY'] = 'ihaveboainmyroom'

    return boa
