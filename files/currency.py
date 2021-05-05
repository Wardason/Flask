from flask import Flask, Blueprint, render_template, request
from forex_python.converter import CurrencyRates

currency = Blueprint('currency', __name__)

c = CurrencyRates()
usd = c.get_rate('EUR', 'USD')
pound = c.get_rate('EUR', 'GBP')
yen = c.get_rate('EUR', 'JPY')
franc = c.get_rate('EUR', 'CHF')
yuan = c.get_rate('EUR', 'CNY')


@currency.route('/currency', methods=['GET', 'POST'])
def convert():

    if request.method == 'POST':
        number_input = request.form['number_input']
    else:
        number_input = request.args.get('number_input')

    if request.method == 'POST':
        currency_input = request.form['currency_input']
    else:
        currency_input = request.args.get('currency_input')


    if currency_input == 'usd':
        converted_amount = float(number_input) * usd
        print(converted_amount)





    return render_template('currency.html')









