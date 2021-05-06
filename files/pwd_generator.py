from flask import Flask, Blueprint, render_template, request
import os

pwd_generator = Blueprint('pwd_generator', __name__)


@pwd_generator.route('/password', methods=['GET', 'POST'])
def generator():
    return render_template('pwd_generator.html')
