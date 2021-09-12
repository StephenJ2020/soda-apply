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
            {"full_name": request.form.get("full_name").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("user_registration"))
        user_registration = {
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
            "diploma result": "",
            "jobs_applied":[]
        }
        mongo.db.users.insert_one(user_registration)
        """
        start a session for the user with a session cookie
        """
        session["user"] = request.form.get("full_name").lower()

        flash("Thanks for joining Soda-Apply!") #should we add another step here for 'proceed to create profile'?
        return redirect(url_for("user_create_profile", user=session["user"]))

    return render_template('pages/user_registration.html')


@app.route("/user_create_profile", methods=["GET", "POST"])
def user_create_profile():
    if request.method == "POST":
        user=session["user"]
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
        mongo.db.users.update_one(
            {"_id": ObjectId()}, personalise_details, upsert=True) 
        
    return render_template('pages/user_create_profile.html', user=session["user"])


@app.route("/user_edit_profile")
def user_edit_profile():
    return render_template('pages/user_edit_profile.html')


@app.route("/login")
def login():
    if request.method == "POST":
        """
        checks if user is already a member in the database
        """
        existing_user = mongo.db.users.find_one(
            {"full_name": request.form.get("full_name").lower()})
        
        if existing_user:
            """
            checks password is correct
            """
            if check_password_hash(
                    existing_user["password"], request.form.get(
                        "password")):
                session["user"] = request.form.get("full_name").lower()
                return redirect(url_for(
                    "profile", full_name=session["user"]))

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

@app.route("/contact")
def contact():
    return render_template('contact.html', page_title="Contact Us")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)  # change to False before submitting