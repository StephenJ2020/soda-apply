import os
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
    return render_template('pages/index.html')


@app.route("/user_registration")
def user_registration():
    return render_template('pages/user_registration.html')


@app.route("/user_create_profile")
def user_profile_create():
    return render_template('pages/user_create_profile.html')


@app.route("/job_listings/")
def job_listings():
    """
    Allow users to see all job listings
    """
    jobs_list = list(mongo.db.jobs.find())

    # if session['user']:
        # user = mongo.db.users.find_one({'full_name': 'Gemma Sayers'})
        # jobs = list(mongo.db.jobs.find())
        # jobs_applied = list(mongo.db.users.find({'jobs_applied': { '$in': jobs[1],} }))
    return render_template('pages/job_listings.html', jobs_list=jobs_list)


@app.route("/job_details/<job_id>", methods=['GET', 'POST'])
def job_details(job_id):
    """
    Allow user to view the complete job description
    """
    user = mongo.db.users.find_one({'full_name': 'Gemma Sayers'})
    job = mongo.db.jobs.find_one({'_id': ObjectId(job_id)})

    if request.method == 'POST':
        user = mongo.db.users.find_one({'full_name': 'Gemma Sayers'})

    return render_template('pages/job_details.html', jobs=jobs, job=job, user=user)


@app.route('/job_application/<job_id>', methods=['GET', 'POST'])
def job_applied(job_id):
    """ 
    Stores data record that the user applied for a job. 
    Stores the job into job_applied data array.
    """
    # user = mongo.db.jobs.find_one({'_id': ObjectId(user_id)})
    # user = mongo.db.users.find_one({'full_name': 'Gemma Sayers'}) 
    user_jobs = []

    if request.method == 'POST':
        job = mongo.db.jobs.find_one({'_id': ObjectId(job_id)}) 
        user_jobs.append(job['role'])

        # mongo.db.users.update({'_id': ObjectId(user_id)}, {
        #                       '$push': {'jobs_applied': user_jobs[0],}})
        mongo.db.users.update({'full_name': 'Gemma Sayers'}, {
                              '$push': {'jobs_applied': user_jobs[0],}})
        print(user_jobs)

    return redirect(url_for('job_listings'))


if __name__ == "__main__":
    app.run(
        host = os.environ.get('IP'),
        port = os.environ.get('PORT'),
        debug = True
    )
