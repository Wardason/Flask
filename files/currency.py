from flask import Flask, Blueprint, render_template, request

currency = Blueprint('currency', __name__)


@currency.route('/currency', methods=['GET', 'POST'])
def convert():

    if request.method == 'POST':
        number_input = request.form['number_input']
        print(number_input)

    if request.method == 'POST':
        currency_input = request.form['currency_input']
        print(currency_input)





    return render_template('currency.html')
