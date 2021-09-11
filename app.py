import os
from flask import Flask, flash, render_template,
redirect, request, session, url_for


app = Flask(__name__)

user = mongo.db.users.find_one(
        {"_id": ObjectId(user)})


@app.route("/")
def index():
    return render_template('pages/index.html')


@app.route("/user_registration")
def user_registration():

    if request.method == "POST":
        
        user_registration = {
            #user object goes here check agains DB before PR
            "full_name": request.form.get("full_name"),
            "email": request.form.get("email"),
            "password": generate_password_hash(request.form.get("password")),
            #password2 - not sure how to use this - does it get created here?
            "created_at": #timestamp - not sure how to implement,
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
        return redirect(url_for("user_create_profile", user_name=session["user"]))

    return render_template('pages/user_registration.html')


@app.route("/user_create_profile/<user>")
def user_create_profile(user):
    if request.method == "POST"
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
            {"_id": ObjectId(user)}, personalise_details, upsert=True) 


    return render_template('pages/user_create_profile.html', user=user)



@app.route("/user_edit_profile<user>")
def user_edit_profile():
    return render_template('pages/user_edit_profile.html')


if __name__ == "__main__":
    app.run(
        host = os.environ.get('IP', '127.0.0.1'),
        port = os.environ.get('PORT', '5000'),
        debug = True
    )