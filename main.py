from flask import Flask, render_template
from files.currency import currency
from files.pwd_generator import pwd_generator


app = Flask(__name__)

app.register_blueprint(currency)
app.register_blueprint(pwd_generator)



@app.route("/")
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(port=1337, debug=True)
