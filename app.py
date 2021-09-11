import os
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    return render_template('pages/index.html')


@app.route("/user_registration")
def user_registration():
    return render_template('pages/user_registration.html')




if __name__ == "__main__":
    app.run(
        host = os.environ.get('IP', '127.0.0.1'),
        port = os.environ.get('PORT', '5000'),
        debug = True
    )