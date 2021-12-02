from flask import Blueprint, render_template, request, flash

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


        if len(boa_inital) < 3:
            flash('Boa_name must be longer than 2 characters.', category = 'badBoa')
        elif len(boa_color) < 2:
            flash('Boa_color must be longer than 1 character.', category = 'badBoa')
        elif len(boa_size) < 4:
            flash('Boa_size must be longer than 3 characters.', category = 'badBoa')
        elif len(boa_sequence1) < 7:
            flash('Boa_sequence must be longer than 6 characters.', category = 'badBoa')
        elif boa_sequence1 != boa_sequence2:
            flash('Boa_sequences do not match.', category = 'badBoa')
        else:
            # create boa
            flash('Boa Created Sucessfully!', category = 'boaGood')



    return render_template("register.html")