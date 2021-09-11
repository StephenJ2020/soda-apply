![CI logo](static/images/readme/soda-hackathon.jpg)   
![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)  


[SODA Apply](https://soda-apply.herokuapp.com/)
Don't just apply, SODA Apply!

# Soda-Apply
------
## Table of Contents
------

* Strategy
* User Stories
* Client Goals
* Scope
* Features & Functional Requirements
* Security
* Data Management
* Content and Structure requirements
* Structure
* Conceptual Design
* Database Schema
* Skeleton
* Wireframes
* Design Inspiration and color choices
* Typography
* Imagery
* Core Features
* Future Implementations
* Bugs & Fixes
* Implementation
* Deployment
* To deploy to Heroku
* Forking the GitHub Repository
* Making a Local Clone
* Testing
* Technologies Used
* Languages Used
* Frameworks, Libraries, Programs & Platforms Used
* Credits
* Acknowledgements


## Strategy
------

As part of the Trust in Soda Hackathon with the Code Institute, the following brief was given;

* Create a tool that helps employers create a truly accessible workspace, or improve their recruitment and onboarding   experience for every person.*
	
>Soda-Apply aims to solve the following issues in the
>recruitment of people with disabilities.  
	
* Issue 1)  	Excluding potential applicants based on advertising methods.
* Issue 2)   	Measurement of an applicant's potential based on the interview environment. 

**The main goal of the Soda-Apply app is to:**

* Simplify the user process of job application
* Simplify explanation of specific requirements / assistive technologies needed for interview process / work environment.
* Creating a profile once in the accessibly designed platform.
* Ability to share the profile directly 

	**Real World usage:**  

>We envisage that Soda-Apply would become a plugin for HR companies and larger corporations with the user able 
>to ‘Soda-Apply’ through a button on the HR / Corp website to submit details in a single click.  


## Primary USER -  Job seeker with disability/ies
------
**As a first time user I would like to:**
* Have a clear indication of the purpose of the site
* Be able to register with a well labelled regular spaced form
* Be able to ‘show password’
* Be presented with clear concise bullet points / not long-winded sentences
* Be able to move throughout the site without animation / video / sound unless chosen 
* Be able to use the site easily with

**Nice to have:**

* Ability to change the colour scheme to suit needs
* Ability to enlarge the text and buttons with a single click.


**As a repeat user I would like to:**
* Easily access and edit my profile 
* See what jobs I have applied to 
* Not be shown jobs that I have already applied to
* Contact Soda-Apply if I need further assistance
* Contact Soda-Apply if I have a recommendation for improvement of the process. 

## Client User Goals - HR company 
------
* To be able to normalise / simplify the recruitment process for people with disabilities 
* To be able to consider accessibility requirements in advance to reach a match for the person / role seamlessly. 
* To promote the company as an accessible recruiter so as not to miss out on the 20% of people worldwide who have accessibility requirements. 

## As a recruiter I would like to be able to:
* Put potential candidates at ease
* View the candidates skills or CV 
* Understand accessibility requirements for application process
* Understand accessibility requirements for interview process
* Understand accessibility requirements for thriving in a potential role. 


## Scope
------

### Features & Functional Requirements
------

* About page to explain the reason for the site
* Registration page to create a profile
* Ability to upload a CV to the profile - preferably in multiple formats
* Profile page that can be edited / updated / deleted
* Jobs listings 
* Admin access page to edit content / listing / profiles if further assistance is needed 
* Partners page to list recruitment partners 
* Contact us ability 

### Accessibility Specific & a11y features
------

* Accessify testing
* Accesslint:
How it works
AccessLint brings automated web accessibility testing into your development workflow. When a pull request is opened, AccessLint reviews the changes and comments with any new accessibility issues, giving you quick, timely, and targeted feedback, before code goes live.
* Lighthouse accessibility will also be an key factor in assessing the app.

#### Security
------
The profile pages should only have edit and delete functionalities for:
* Admin / superuser
* Profile creator
* Werkzeug will be used for password hashing
* Sessions will be used 

Others should not be able to access the profile (for example by url). 


#### Data Management
------

Postgres will be used as the relational database for storing the data of the user profiles. 
It will be necessary to:

* **ensure there is no one step deletion** of data and that **delete buttons are labelled** (not just icons)

* Access functionality managed through app routes and jinja templating to make use of session user cookies, but also data matching

#### UX
------

The app should employ features for accessibility inline with the User Story requirements. 

## Structure
------

#### Conceptual Design
------
(add a user flow-chart here including CRUD operations)

#### Database Schema 
------
(add database schema here)

#### Skeleton
------


#### Wireframes
------
* Wireframes were created using the [Balsamiq](https://balsamiq.com/wireframes/) software.

**Home Page**

![Home](docs/wireframes/Home.png)

* The Home page features a Hero Image with a call to action, prompting users to create an account with SODA Apply.
* The About US sections allows users to get to know us and immediately know that accessability is our number one priority.
* Using Roboto font, a monochromatic color palette and lots of white space provide demonstrate an accessible appearance.


**Profile Page**

![Profile](docs/wireframes/Profile.png)

* The profile page is designed to be a scrollable page with easy access to the various sections.
* Links to all sections are at the top of the profile page with back-to-top links.


All wireframes.
* [Home](docs/wireframes/Home.png)
* [Profile](docs/wireframes/Profile.png)
* [Jobs](docs/wireframes/Jobs.png)
* [Job-Details](docs/Job-Details/Profile.png)
* [Register](docs/wireframes/Register.png)
* [Log In](docs/wireframes/login.png)
* [Contact Us](docs/wireframes/Contact-us.png)
* [FAQ](docs/wireframes/FAQ.png)

A pdf of the wireframes can be found [here](doc/wireframes/soda-apply_wireframes.pdf), by clicking on the download button in Github. (**Please Note:** _[Adobe Acrobat Reader](https://get.adobe.com/reader/) is required to view files in pdf format_).

#### [Back to top](<#table-of-content>)


#### Design Inspiration & Colour choices
------
Theme for design and colour choices was taken from looking at other sites that score well on the accessibility in google lighthouse, as well as wanting the look to be inline with the Client themes - In this case Trust in Soda.  
#### Typography
------
Fonts must be accessible leading to a choice of Roboto & Arvo accessible text imports. 

#### Imagery
------
**(imagery chose goes here)**


#### Core Features
------
* Simply designed home page
* Registration form designed for utmost accessibility with profile questions relating to easing the recruitment process f for the candidate. 
* Upload CV to profile page
* Share profile with potential employers (in read only format)
* Ability to edit or delete profile as user of said profile or as an admin
(potentially) API link to jobs 
* Simply designed FAQ’s
* Contact us functionality


#### Future Implementations
------

* Create as a plug-in for HR or Corporate recruiters. 


#### Bugs & Fixes
------
**Bugs and fixes to go here**


#### Implementation
------


#### Deployment
------
This project was built using Gitpod and pushed to Github using the terminal interface. However, as Github can only host static websites the project had to be deployed to Heroku as it is compatible for hosting a back-end focused site.  

This project was deployed using Heroku and stored in GitHub.

Before deploying the website to Heroku, the following three must be followed to ensure that the app will work in Heroku:  
  
1. Create requirements.txt file that contains the names of packages being used in Python. It is important to update this file if other packages or modules are installed during project development by using the following command:

    - pip freeze --local > requirements.txt

2. Create Procfile that contains the name of the application file so that Heroku knows what to run. If the Procfile has any blank lines they should be removed as they may cause issues.

3. Push these files to the project Repo in GitHub.  
  
Once those steps are done, the website can be deployed in Heroku using the steps listed below:

### Deployment Steps

1. Log into Heroku.
2. Click the New button.
3. Click the option to create a new app.
4. Enter the app name in lowercase letters.
5. Select the correct geographical region.

### Set environment variables:
  
Navigate to the settings tab and then click the Reveal Config Vars button and add the following:
  
1. key: IP, value: 0.0.0.0
2. key: PORT, value: 5000
3. key: MONGO_DBNAME, value: (the name of the database that is being used for the project)
4. key: MONGO_URI, value:
 * This can be found in MongoDB by navigating  to the clusters section of your MongoDB account.
 * Click the cluster where the database is located.
 * Click the connect button.
 * Select the connect you application button.
 *  Copy the link provided to your application and ensure you have substituted the password and dbname with the correct values).
5. key: SECRET_KEY, value: (This is a custom secret key set up for configuration to keep client-side sessions secure).


### Enable automatic deployment:

1. Click the Deploy tab  
    
2. In the Automatic deploys section, choose the branch you want to deploy from then click Enable Automation Deploys.
 


### Connect app to Github Repository

1. Click the deploy tab and connect to GitHub.  
  
2. Type the name of the repository into the search bar presented.  
      
3. Click the Code dropdown button next to the green Gitpod button.  
  
4. When the correct repository displays click the connect button.  



### Making a clone to run locally

It is important to note that this project will not run locally unless an env.py file has been set up by the user which contains the IP, PORT, MONGO_DBNAME, MONGO_URI and SECRET_KEY which have all been kept secret in keeping with best security practices. 

1. Log into GitHub.
2. Select the [respository](https://github.com/StephenJ2020/soda-apply).  
3. Click the Code dropdown button next to the green Gitpod button.
4. Download ZIP file and unpackage locally and open with IDE. Alternatively copy the URL in the HTTPS box.
5. Open the alternative editor and terminal window.
6. Type 'git clone' and paste the copied URL.
7. Press Enter. A local clone will be created.

Once the project been loaded into the IDE it is necessary to install the necessary requirements which can be done by typing the following command.

    -pip install -r requirements.txt

### How to Fork the respository.

By forking the GitHub Repository you make a copy of the original repository on your own GitHub account to view and/or make changes without affecting the original repository by following these simple steps:

1. Log in to GitHub and locate the [StephenJ2020/soda-apply Repository](https://github.com/StephenJ2020/soda-apply)
2. Near the top of the Repository, on the right-hand side of the screen, locate the "Fork" button.
3. Click this button and you should now have a copy of the original repository in your GitHub account.
  
### Making a Local Clone

1. Log in to GitHub and locate the [StephenJ2020/soda-apply Repository](https://github.com/StephenJ2020/soda-apply)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.
```
$ git clone https://github.com/StephenJ2020/soda-apply
```
7. Press Enter. Your local clone will be created.
```
$ git clone https://github.com/StephenJ2020/soda-apply
> Cloning into `CI-Clone`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
``` 

#### Testing
------


#### Technologies Used
------
* Languages Used:
	* HTML5
	* CSS3
	* Javascript
	* Python
* Frameworks, Libraries, Programs & Platforms Used:
		* Flask
		* Postgres
		* Bootstrap5
		* Jinja

#### Credits
------

#### Acknowledgements
------