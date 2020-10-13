# PythonBot

### Instabot :

This is a instagram bot written in python. This will go though a list of user or hashtags, and like the posts in order to generate visits on your instagram accounts.

### Soundcloudbot :

Sondcloud bot written in python. Will go a list of user and follow them. The unfollow script is there too. Will help generate trafic on the users pages.

## How to Install it

### Package Manager

I would always recommand using `npm` (node package manager) which come with the install of `node.js`.</br>
Nevertheless the python specific package manager `pip` is here mandatory for some package (see below).</br>
And now that you are at it, install `brew` if you don't have it yet, as we will need it to get `python3`. </br>
</br>
To updagrade pip3, run `pip3 install --upgrade pip`.

### What to install and how to do it

The whole thing can't run without Python: `brew install python3`, to get the lattest python version (incl. `pip3`).</br>

#### Instabot:

The two most important package are `instabot` and `instagramapi`. Use pip3 to install those. </br>
In case of admin rights problem, you may want to _sudo_ it.</br>

```
sudo pip3 install instabot
sudo pip3 install instagramapi
```

#### Soundcloudbot:

For running craeler and code directly with a browser, install `selenium`.</br>
Save the chromedriver in the right folder. Per default, this executable is saved under "/ressources". This is a lightweight version of Chrome and will be controlled by the script.

## Deployment

To create the Docker file : `docker build -t instabot-cvs . `
List to all the commandline for docker: https://docs.docker.com/engine/reference/commandline/
Most useful: `docker image list` and `docker image rm your-docker-file`.

To deploy a docker file on Heroku:

```
$ heroku login
$ heroku container:login
$ heroku container:push web --app instabot-cvs
$ heroku container:release web
```

Ressources on deploying Docker on Heroku: https://devcenter.heroku.com/articles/container-registry-and-runtime

## Under the hood

### How to start the script

Open a terminal, place yourself in the folder where to code is and run the script with python using the following command : </br>

```
caffeinate python3 instabot.py
```

_Caffeinate_ is used to stop the computer from going to sleep modus. </br>
</br>
Use -i to interact with python code. </br>

```
caffeinate -i python3 soundcloudbot.py
```

### Sending mail with Python

Some mail are getting sent from the code, mainly to alert the admin of failure when running the code. </br>
I used this ressoruce to set it up: https://realpython.com/python-send-email/

#### Allow gmail to be access by less secured apps:

By toggling this : https://myaccount.google.com/lesssecureapps

### Logging

The levels of logs:

- DEBUG: Detailed information, typically of interest only when diagnosing problems.
- INFO: Confirmation that things are working as expected.
- WARNING: An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.
- ERROR: Due to a more serious problem, the software has not been able to perform some function.
- CRITICAL: A serious error, indicating that the program itself may be unable to continue running.

Quite complete tutorial about the logging feature of python: https://www.datadoghq.com/blog/python-logging-best-practices/

### Python and postgreSQL

#### Install

To install to postgreSQL driver "psycopg2" run: `pip3 install psycopg2-binary`.

#### Login

The file configDB.py containt a fonction reading the config data from fiöe database.ini

#### SQL

To insert data : `INSERT INTO public.userlist_myUserName(username) VALUES ('anyInstaProfil');`.
The column ùsername`has a type Char Variable (30), as we assume that a instagram login can't be longer than 30 characters.

## Errors

### Error code comming from InstagramAPI

#### Blocked account for spam:

```
Request return 400 error!
{'message': 'feedback_required', 'spam': True, 'feedback_title': 'Try Again Later', 'feedback_message': 'We restrict certain activity to protect our community. Tell us if you think we made a mistake.', 'feedback_url': 'repute/report_problem/instagram_like_add/?violation_type&responsible_policy=Ig.Policy.Engagement.SessionClassifier.SessionClassifierRunPrediction', 'feedback_appeal_label': 'Tell us', 'feedback_ignore_label': 'OK', 'feedback_action': 'report_problem', 'category': 'instagram_like_add', 'status': 'fail'}
```

#### Private user:

```
Request return 400 error!
{'message': 'Not authorized to view user', 'status': 'fail'}
```

## Links

- Repository on git hub: https://github.com/vanStaen/clembot
- Ressource about the library: https://recycledrobot.co.uk/words/?instaspam
- how to write a docker file: https://www.educative.io/edpresso/how-do-you-write-a-dockerfile

## todo

- Deploy docker node app to heroku: https://www.youtube.com/watch?v=6l55lOyerZk
- Build & Deploy A Python Web App | Flask, Postgres & Heroku: https://www.youtube.com/watch?v=w25ea_I89iM
- Automate Spotify with Python: https://www.youtube.com/watch?v=7J_qcttfnJA
- Cronjob on heroku with python: https://saqibameen.com/deploy-python-cron-job-scripts-on-heroku/
