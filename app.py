import os
from flask import (Flask, flash, render_template,
redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

#user = mongo.db.users.find_one()


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
def index():
    return render_template('pages/index.html')


@app.route("/user_registration", methods=["GET", "POST"])
def user_registration():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"email": request.form.get("email").lower()})

        if existing_user:
            flash("Email already exists")
            return redirect(url_for("user_registration"))

        registration = {
            "full_name": request.form.get("full_name").lower(),
            "email": request.form.get("email"),
            "password": generate_password_hash(request.form.get("password")),
            #"created_at": datetime.datetime.now(),
            "about": "",
            "company_name": "",
            "role_title": "",
            "months_employed": 0,
            "accessible_hiring_preferences": [],
            "other_acc_hiring_preferences": "",
            "skills_competencies": [],
            "institute_name": "",
            "course_title": "",
            "diploma_result": "",
            "jobs_applied":[]
        }
        mongo.db.users.insert_one(registration)
        """
        start a session for the user with a session cookie
        """
        session["user"] = request.form.get("email").lower()

        flash("Thanks for joining Soda-Apply!")
        return redirect(url_for("user_create_profile", user=session["user_id"]))

    return render_template('pages/user_registration.html')


@app.route("/user_create_profile/<user_id>", methods=["GET", "POST"])
def user_create_profile(user_id):  
    if request.method == "POST":
        user = mongo.db.users.find_one(
            {"_id": session["user"]})

        personalise_details = {"$set": {
            "about": request.form.get("about"),
            "company_name": request.form.get("company_name"),
            "role_title": request.form.get("role_title"),
            "months_employed": request.form.get("months_employed"),
            "accessible_hiring_preferences": request.form.getlist("accessible_hiring_preferences"),
            "other_acc_hiring_preferences": request.form.get("other_acc_hiring_preferences"),
            "skills_competencies": request.form.getlist("skills_competencies"),
            "institute_name": request.form.get("institute_name"),
            "course_title": request.form.get("course_title"),
            "diploma_result": request.form.get("diploma_result")
        }}
        mongo.db.users.update_one(
            {"_id": ObjectId(user)}, personalise_details)
        flash("thanks for personalising your Soda-Apply profile.")
    return render_template('pages/user_create_profile.html', user=user)


@app.route("/profile/<user>")
def profile(user):
    return render_template('pages/profile.html', user=user)

@app.route("/user_edit_profile<user>")
def user_edit_profile():
    return render_template('pages/user_edit_profile.html')

@app.route("/contact")
def contact():
    return render_template('contact.html', page_title="Contact Us")


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