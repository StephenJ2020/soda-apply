import os
import json
import random
from flask import (
    Flask, render_template, flash, redirect,
    request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
def index():
    partnerdata = []    
    with open("data/partner.json", "r") as json_partnerdata:
        partnerdata = json.load(json_partnerdata)
        random.shuffle(partnerdata)
    return render_template('pages/index.html', partners=partnerdata)


@app.route("/user_registration")
def user_registration():
    return render_template('pages/user_registration.html')


@app.route("/user_create_profile")
def user_profile_create():
    return render_template('pages/user_create_profile.html')


@app.route("/contact")
def contact():
    return render_template('pages/contact.html', page_title="Contact Us")


@app.route("/job_listings")
def job_listings():
    """
    Allow users to see all job listings
    """
    jobs = list(mongo.db.jobs.find())
    return render_template('pages/job_listings.html', jobs=jobs,)


@app.route("/job_details/<job_id>", methods=['GET', 'POST'])
def job_details(job_id):
    """
    Allow user to view the complete job description
    """
    job = mongo.db.jobs.find_one({'_id': ObjectId(job_id)})
    jobs = list(mongo.db.jobs.find())
    return render_template('pages/job_details.html', jobs=jobs, job=job,)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)  # change to False before submitting