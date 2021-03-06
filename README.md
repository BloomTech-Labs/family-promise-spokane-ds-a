
# Family Promise of Spokane

Welcome to the Data Science Team B's repository for the Family Promise of Spokane Project! This repository holds all the source code for our API as well as the predictive model used by the app.

# Description

The Family Promise of Spokane is a US-based nonprofit organization based in Spokane, WA. They are an organization that aims to curb homelessness for families through both corrective and preventive measures. Their services include providing shelter for families as well as rental assitance. For more details of the organizations and the amazing work they do, be sure to check out their [website](https://www.familypromiseofspokane.org/)

# Contributors

## Data Science Team

| [Kristine Wang](https://github.com/KristineYW) | [Tyler Etheridge](https://github.com/tyleretheridge) | [Santiago Berniz](https://github.com/sberniz/) | [Christopher Lee](https://github.com/chrislee973) |
| :---: | :---: | :---: | :---: | 
| [<img src="https://avatars0.githubusercontent.com/u/63246056?s=400&u=a10524916b756eb26132d0803bec3cbe62ede1ef&v=4" width = "200" />](https://github.com/KristineYW) | [<img src="https://avatars3.githubusercontent.com/u/61953470?s=400&u=8f8538f4d10dcb45b9179eb6990d1ef9c1aadc8d&v=4" width = "200" />](https://github.com/tyleretheridge) | [<img src="https://avatars3.githubusercontent.com/u/6207914?s=460&u=8bfaa068f7942170423371ff10e8f04f09f41e81&v=4" width = "200" />](https://github.com/sberniz/) | [<img src="https://avatars.githubusercontent.com/u/44345856?s=460&u=d27781ca6a5d01414c4ffbe7e0ac9986e3acd114&v=4" width = "200" />](https://github.com/chrislee973) |
| TPL | Data Scientist | Data Scientist | Data Scientist | 
|[<img src="https://github.com/favicon.ico" width="15"> ](https://github.com/KristineYW) | [<img src="https://github.com/favicon.ico" width="15"> ](https://github.com/tyleretheridge) | [<img src="https://github.com/favicon.ico" width="15"> ](https://github.com/sberniz/) | [<img src="https://github.com/favicon.ico" width="15"> ](https://github.com/chrislee973) |
| [ <img src="https://static.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" width="15"> ](https://www.linkedin.com/in/kristine-wang-ds/) | [ <img src="https://static.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" width="15"> ](https://www.linkedin.com/in/tylerjetheridge/) | [ <img src="https://static.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" width="15"> ](https://www.linkedin.com/in/santiago-berniz/) | [ <img src="https://static.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" width="15"> ](https://www.linkedin.com/in/chrislee973/) |          

| [Ik Okoro](https://github.com/ik-okoro) | [Justin Rivest](https://github.com/jrivest2) |
| :---: | :---: |  
| [<img src="https://ca.slack-edge.com/ESZCHB482-W019Y5BRPEC-c1d88c2f8d2c-512" width = "200" />](https://github.com/ik-okoro) | [<img src="https://avatars.githubusercontent.com/u/55200197?s=460&u=3593bf0d5d9e919a817dd057345f0c5e35f1c6da&v=4" width = "200" />](https://github.com/jrivest2) | 
| Data Scientist | Data Scientist | 
|[<img src="https://github.com/favicon.ico" width="15"> ](https://github.com/ik-okoro) | [<img src="https://github.com/favicon.ico" width="15"> ](https://github.com/jrivest2) | 
| [ <img src="https://static.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" width="15"> ](https://www.linkedin.com/in/ik-okoro-ml-engineer) | [ <img src="https://static.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" width="15"> ](https://www.linkedin.com/in/justinrivest/) |              

<br>          

<br>
<br>

## Libraries
![fastapi](https://img.shields.io/badge/fastapi-0.60.1-blue)
![uvicorn](https://img.shields.io/badge/uvicorn-0.11.8-ff69b4)

![sqlalchemy](https://img.shields.io/badge/sqlalchemy-1.3.23-00cc96)
![python-dotenv](https://img.shields.io/badge/python--dotenv-0.14.0-green)

![pandas](https://img.shields.io/badge/pandas-1.1.0-blueviolet)
![scikit-learn](https://img.shields.io/badge/scikit--learn-0.22.2.post1-yellow)
![plotly](https://img.shields.io/badge/plotly-4.14.3-ab63fa)



# Deployments

As long as the sites are still hosted, you can find the deployments for each of the three branches of the full product below. Otherwise, to view source code or deploy locally, please see the linked repositories instead in the next section.  

[Front End Dashboard](https://b.familypromisesofspokane.dev/) |
[Data Science API](https://b-ds.familypromisesofspokane.dev/) |
[Back End API](https://family-promise-spokane-be-b.herokuapp.com/) |

# Linked Repositories

[Family Promise of Spokane Front end](https://github.com/Lambda-School-Labs/family-promise-spokane-fe-b) | 
[Family Promise of Spokane Back End](https://github.com/Lambda-School-Labs/family-promise-spokane-be-b) |


# Getting Started

## Setup Instructions

In your CLI, clone the repository to your local machine using:

    git clone <repository link>

In order for the app to function correctly, the user must set up valid environment variables. There should be a .env file  in the root project directory containing the following:

    SQLALCHEMY_DATABASE_URL = Postgres database credentials

To run the FastAPI app from your CLI, use:

    uvicorn app.main:app --reload

You should be able to see the app running in your [localhost](http://127.0.0.1:8000) after application startup is complete.


<!--### User Flows

[Trello Board](https://trello.com/b/FyWvcZzY/family-promise-of-spokane)

Our team is developing a digital intake form for families in Family Promise Shelter. This intake form is a replacement for the paper form currently being filled by guests of the shelter. All the Data is given by the guests. We have a multi-class random forest model that takes the guest data and predicts their exit destination. The possible Exit Destination are as follow. 
- Permanent Exit
- Temporary Exit
- Emergency Shelter
- Transitional Housing
- Unknown/Other

### Key Features

- Supervisors can Create guest profile 
- Case Manager can view guest profile 
- Case Manager can view the exit destination prediction
- Guest can be flagged for mis conduct
- notes can be added to guest's profile. 
- Guest can view their own profile. 
### Environment Variables




### Content Licenses

| Image Filename | Source / Creator | License                                                                      |
| -------------- | ---------------- | ---------------------------------------------------------------------------- |
| Nopic.yet      | INSERT NAME      | [MIT](input githandle here)                             |
-->
<!--
### Installation Instructions

We used Docker for ease of use when dealing with environmental dependancies 

#### Scripts

    Get AWS credentials
    
    Get your AWS access keys
    
    Install AWS Command Line Interface
    
    * aws configure -> configures AWS CLI
    * pip install pipx -> installs pipx
    * pipx install awsebcli -> installs AWS Elastic BeanStalk CLI
[Follow AWS EB docs](https://docs.labs.lambdaschool.com/data-science/tech/aws-elastic-beanstalk)
    
    Then use the EB CLI:
    
    * git add --all 
    * git commit -m "Your commit message" 
    * eb init -p docker YOUR-APP-NAME --region us-east-1 
    * eb create YOUR-APP-NAME 
    * eb open 
    
    Then use AWS Route 53 to set up a domain name with HTTPS for your DS API
    
    Redeploy:
    
    * git commit ... 
    * docker build ... 
    * docker push ... 
    * eb deploy 
    * eb open 
-->
# Tech Stack

### Data Science API built using:

- Python
- Docker
- FastAPI
- AWS Elastic Beanstalk
- PostgreSQL
- Pipenv

### Why we made our tech stack decisions:

- Wanted to gain insight to AWS
- Docker and Pipenv makes environments easier
- FastAPI has been gaining traction over Flask
- SQL queries are better structured 


# User Flow

### Data Science API

We are receiving a POST request with the member id from the web team and using that id to query the database, choose the features used to create the classification model, predict the exit destination and returning a prediction for the exit destination along with the top features in JSON format. 

# Architecture Chart
![Architecture](https://github.com/Lambda-School-Labs/family-promise-spokane-ds-a/raw/main/architecture_diagram2.png)




# End Points
/predict: send POST request to this endpoint with the member_id value. 

# Issues
**If you are having an issue with the existing project code, please submit a bug report under the following guidelines:**

- Check first to see if your issue has already been reported.
- Check to see if the issue has recently been fixed by attempting to reproduce the issue using the latest master branch in the repository.
- Create a live example of the problem.
- Submit a detailed bug report including your environment & browser, steps to reproduce the issue, actual and expected outcomes, where you believe the issue is originating from, and any potential solutions you have considered.


# Support
Santiago and Tyler on slack. 

### Contributing

When contributing to this repository, please first discuss the change you wish to make via issue, email, or any other method with the owners of this repository before making a change.

Describe what you have changed in this repo as a team
Provide examples and descriptions of components, how props are handled, where to find these changes, database tables, models, etc.

### Feature Requests

We would love to hear from you about new features which would improve this app and further the aims of our project. Please provide as much detail and information as possible to show us why you think your new feature should be implemented.

### Pull Requests

If you have developed a patch, bug fix, or new feature that would improve this app, please submit a pull request. It is best to communicate your ideas with the developers first before investing a great deal of time into a pull request to ensure that it will mesh smoothly with the project.

Remember that this project is licensed under the MIT license, and by submitting a pull request, you agree that your work will be, too.

#### Pull Request Guidelines

- Ensure any install or build dependencies are removed before the end of the layer when doing a build.
- Update the README.md with details of changes to the interface, including new plist variables, exposed ports, useful file locations and container parameters.
- Ensure that your code conforms to our existing code conventions and test coverage.
- Include the relevant issue number, if applicable.
- You may merge the Pull Request in once you have the sign-off of two other developers, or if you do not have permission to do that, you may request the second reviewer to merge it for you.

### For future cohorts*\
Our team in Labs 31 was the third iteration of this Labs project and for almost the first two weeks, we were solving the puzzle of what was left behind for us. Hopefully this ReadME would help you to hit the ground running. Everything is divided into the appropriate section below.

To start, it would help to look at all the previous cohorts roadmaps to have a sense of their deliverables. This was huge in helping us fill some of the puzzle pieces.

First, the models. There's a few pickled models in the repos from versions 1 to 4. As we came to understand it, v1 and v2 were created by Labs 29 and trained on not enough features to satisfy Labs 30 team. They then created v3 and v4 training them on more features but not a significant increase in accuracy. V4 never got implemented by Labs 30 because it was trained on features in the historical data that weren't in the DB and differed in data format for some of the features that were common to both the historical data and DB. Unfortunately, we noticed there's leakage in all 4 models due to the shuffled split. Multiple family members from one family id end up in the train and test sets. Getting rid of any leakage results in a virtually baseline accuracy of ~40%. That's the model we had to use and you can find the model and the notebook at *./app/assets/model.pkl* and *./notebooks/Model.ipynb* respectively.

Next is the database and historical data. We had an extra task outside our roadmap the first two weeks to merge the historical data with the database. The historical data is the all_data_with_exits csv file. In the first iteration of this project, the DB was expected to follow the same format as the historical data but something got lost in translation somewhere along the way. It would help to go through the intake form while viewing the database to get a sense of what the DB holds. We view the database with [TablePlus](https://tableplus.com/). In our work to merge the data, we assembled a [Google Doc](https://docs.google.com/document/d/1U2kta5EFHWheiXBFhlNwLo7UwW2FuzEJQ20UF77KRZw/edit) that would hopefully have more answers than questions. As you can see there's multiple problems like inconsistent data in DB from text fields. In an ideal world, a family goes through intake, all data ends up in the DB like in the csv, then our model draws data from the DB to make a prediction. To workaround, an adjacent teammate from Team A created our own Postgres database to use. The link is in our env files but will be forwarded to you. Unfortunately in this process, the original DB Members and Families tables were accidentally overwritten so if it's not fixed, our google docs might be the only idea of what the tables used to look like. With our own DB, we now have the code for a model and the dashboard. If the DB is ever adjusted to what it was originally intended, you'll have the starter code to switch the env variables and make some minor adjustments to have working code. Note that our database mostly uses the members table features and a couple from Families. Note that any unknown integers were saved as -1. Should be able to see the code in Team A's repo. The last exit date in the csv is end of August, 2020 so our code sets "today" as 210 days ago with a timedelta to enable us to pull actual data.

Next is the API. The API we inherited was unfortunately broken and we were not overly satisfied with the code. The shaply plots didn't work either as seen in the demo. We moved everything from the earlier cohorts to old_app and created a new API in /app with as much DRY code as we could using SQLAlchemy's automap.Try deploying locally to see the docs and all the routes.

When deploying to AWS, we had some problems getting our deployment to work. Turns out it was because we created the pipfile lock with Windows. Using the original Pipfile and lock from Team A's earlier cohorts helped with a temporary workaround for our first deployment since it was created on Linux. We also used Docker as the python approach in Lambda docs didn't help either. Simply skip steps 2, 3, and 4 then change *python-3.7* to *docker* in step 7. The python version seems to raise issues with nginx and creating specification files. Docker was more straightforward. The second time deploying, we had a teammate use WSL to do all the pipenv installs and it was smooth sailing.

There's two environments from DS-31-B on AWS. The first is *fam-promise-ds-teamB* which we'll call API 1. The second is *family-promise-ds-31B* which we'll call API 2. API 1 was our first deployment to give the Web team an API to test initial dashboard queries with. It's bare bones in that:
* the "/" route doesn't route to the FastAPI's interactive openapi docs
* works just like it would locally by going to "/docs" to use the interactive docs
* only meaningful routes are the digital dashboard routes for exits, average stay, and income increase
* Never got updated with any new code

API 2 is more complete and:
* has the home route going to the interactive docs
* includes the plotly routes for exits and 90 day exit moving averages
* includes the predict exit route
* Gets updated with any new code

Note that the Web team could get responses from API 2 locally but couldn't from their deployed app. This was before updating the CORS security origins to only allow their deployment to call the API. As a result we left the security open to all in the meantime till that's figured out. Here are the appropriate links for each API:
* API 1: http://fam-promise-ds-teamb.eba-sj7vxixq.us-east-1.elasticbeanstalk.com/
* API 2: https://b-ds.familypromisesofspokane.dev/ (Hosting http://family-promise-ds-31b.eba-k6eubjpn.us-east-1.elasticbeanstalk.com/)

It'll be beneficial to check which API version the web team is using for calls and advise them accordingly.


### Attribution

These contribution guidelines have been adapted from [this good-Contributing.md-template](https://gist.github.com/PurpleBooth/b24679402957c63ec426).

### Documentation
[Front End](https://github.com/Lambda-School-Labs/family-promise-spokane-fe-a/blob/main/README.md)

[Back End](https://github.com/Lambda-School-Labs/family-promise-spokane-be-a/blob/main/README.md)

[Data Science](https://github.com/Lambda-School-Labs/family-promise-spokane-ds-a/blob/main/README.md)
