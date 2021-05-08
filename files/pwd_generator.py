from flask import Flask, Blueprint, render_template, request
import base64
import os

pwd_generator = Blueprint('pwd_generator', __name__)


@pwd_generator.route('/password', methods=['GET', 'POST'])
def generator():
    if request.method == 'POST':
        number_input = request.form['number_input']
    else:
        number_input = request.args.get('number_input')

    length = int(number_input)
    password = base64.b64encode(os.urandom(length)).decode("ascii")
    msg = f'Your password is {password}'

    return render_template('pwd_generator.html', variable=msg)
