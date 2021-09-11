import os

from flask import Flask, render_template
if os.path.exists("env.py"):
    import env
import pymongo


app = Flask(__name__)


@app.route("/")
def index():
    return render_template('pages/index.html')


if __name__ == "__main__":
    app.run(
        host = os.environ.get('IP'),
        port = os.environ.get('PORT'),
        debug = True
    )
    