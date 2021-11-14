from flask import Blueprint, render_template, request

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return '<h1>Logout</h1>'

@auth.route('/register', methods = ['GET', 'POST'])
def register():
    if request.method == 'POST':
        boa_inital = request.form.get('boa_inital')
        boa_color = request.form.get('boa_color')
        boa_size = request.form.get('boa_size')
        boa_sequence1 =  request.form.get('boa_sequence1')
        boa_sequence2 = request.form.get('boa_sequence2')


    return render_template("register.html")