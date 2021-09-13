import os
import random
import json
from flask import (
    Flask, render_template, flash, redirect,
    request, session, url_for)
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
    partnerdata = []   
    with open("data/partner.json", "r") as json_partnerdata:
        partnerdata = json.load(json_partnerdata)
        random.shuffle(partnerdata)    
    jobs = list(mongo.db.jobs.find())
    return render_template('pages/index.html', partners=partnerdata, jobs=jobs)


@app.route("/user_registration", methods=["GET", "POST"])
def user_registration():
    if request.method == "POST":

        existing_user = mongo.db.users.find_one(
            {"email": request.form.get("email").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("user_registration"))

        user_registration = {
            "full_name": request.form.get("full_name").lower(),
            "email": request.form.get("email"),
            "password": generate_password_hash(request.form.get("password")),
            #"created_at": datetime.datetime.now(),
            #"about": "",
            #"company_name": "",
            #"role_title": "",
            #"months_employed": 0,
            #"accessible_hiring_preferences": [],
            #"other_acc_hiring_preferences": "",
            #"skills_competencies": [],
            #"institute_name": "",
            #"course_title": "",
            #"diploma result": "",
            #"jobs_applied":[]
        }
        mongo.db.users.insert_one(user_registration)
        """
        start a session for the user with a session cookie
        """
        session["user"] = request.form.get("email").lower()

        flash("Thanks for joining Soda-Apply!") #should we add another step here for 'proceed to create profile'?
        return redirect(url_for('profile'))

    return render_template('pages/user_registration.html')


@app.route("/user_create_profile/<user_id>", methods=["GET", "POST"])
def user_create_profile(user_id):
    if request.method == "POST":
        user = mongo.db.users.find_one({"_id": ObjectId(user_id)})
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
            "diploma result": request.form.get("diploma result")
        }}
        print(user)
        mongo.db.users.update({"_id": ObjectId(user_id)}, personalise_details)
        
        return render_template('pages/user_create_profile.html', user=user)

    flash("Error")
    return render_template('pages/index.html')


@app.route("/user_edit_profile")
def user_edit_profile():
    return render_template('pages/user_edit_profile.html')

@app.route("/profile")
def profile():
    return render_template('pages/profile.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        """
        checks if user is already a member in the database
        """
        existing_user = mongo.db.users.find_one(
            {"email": request.form.get("email").lower()})
        
        if existing_user:
            """
            checks password is correct
            """
            if check_password_hash(
                    existing_user["password"], request.form.get(
                        "password")):
                session["user"] = request.form.get("email").lower()
                return redirect(url_for("profile", email=session["user"]))

            else:
                """
                if password invalid
                """
                flash("Invalid password and / or username")
                return redirect(url_for("login"))
        else:
            """
            if username invalid
            """
            flash("Invalid password and / or username")
            return redirect(url_for("login"))

    return render_template('pages/login.html')


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))



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



@app.route("/accessibility")
def accessibility():
    return render_template('pages/accessibility.html', page_title="Accessibility Statement")


@app.route("/privacy")
def privacy():
    return render_template('pages/privacy.html', page_title="Privacy Statement")


# Error handlers
@app.errorhandler(404)
def response_404(exception):
    """
    On 404 detection, display custom 404.html template to user
    """
    return render_template('pages/404.html', exception=exception, page_title="404")


@app.errorhandler(500)
def response_500(exception):
    """
    On 500 detection, display custom 500.html template to user
    """
    return render_template('pages/500.html', exception=exception, page_title="500")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)  # change to False before submitting