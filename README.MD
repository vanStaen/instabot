# instaBot

This is a instagram bot written in python. This will go though a list of user or hashtags, and like the posts in order to generate visits on your instagram accounts.

You will find this project online under: https://instabot-cvs.herokuapp.com/

## Add an account

1. Crawl some user for the new account
2. Create a table `userlist_#newaccount` with column `username` in the database
3. Fill the date base with the usernames obtained in 1. To insert value, use the following:

```
INSERT INTO public.userlist_#newaccount(username) VALUES ('?');
```

4. Add the account password in the .env variables
   . Insert a new row as config for the new account:

```
INSERT INTO public.config_accounts_insta(
	active, iterations, tags, username, alive, id)
	VALUES (?, ?, ?, ?, ?, ?);
```

5. Add the account password in the .env variables (local and on the server side)

## Packages & dependancies

To install at one all packege listed in the requirements.txt file, run the following:
`pip3 install -r requirements.txt`

The python specific package manager `pip` is mandatory for the python package . You may need to install `brew` to get `python3`. With brew, go `brew install python3`.</br>

To upgrade pip3 : `pip3 install --upgrade pip`</br>
See the details of a package: `pip3 show <packageneame>`

The two most important package for the instagram bot are `instabot` and `instagramapi`. Use pip3 to install those. In case of admin rights problem, you may want to _sudo_ it. To install those: `sudo pip3 install instabot`and `sudo pip3 install instagramapi`.</br>

All the packages should be listed in the file "requirement.txt".

For reason, I use the `npm run <scripts>` to run custom script, and still have a package.json. Because it worked so far for me. It confuse Heroku on deploy though (because of the Procfile), but is not breaking anything.

## Deployment

Running the following command 'npm run deploy' will trigger the deployment of the master branch.
When deploying on Heroku, you may want to have both python and node.js buildpack initialized. To do so with the Heroki CLI, just run:

```
heroku buildpacks:clear
heroku buildpacks:add --index 1 heroku/python
heroku buildpacks:add --index 2 heroku/nodejs
```

- A procfile is needed (from the python framework) to start a web process running: in our case a node pointing to index.js
- A requirement.txt file containing all needed package. Heroku will need this file to install the dependancies on the server side during the deployment.

## Debugging and logs

Use `heroku logs --tail` when logged on the Heroku CLI , to access all the logs from the server.
If the scheduler is running and the script is throwing error, but won't kill itself:

```
heroku ps
heroku ps:stop <name of the scheduler>
```

## Under the hood

### Cron Job

The command `$ python3 index.py` runs 3 times a day, and `python3 weekly.py` running every morning, both using the scheduler addon, from heroku.

All extra logic (about what dasy of the week the script should run) is included directly in the python sripts.

### How to run the script locally

Open a terminal, place yourself in the folder where to code is and run the script with python using the following command : </br>

```
caffeinate python3 localBot.py
```

_Caffeinate_ is used to stop the computer from going to sleep modus. </br>
</br>
Use -i to interact with python code. </br>

```
caffeinate -i python3 soundcloudbot.py
```

### Sending mail with Python

Some mail are getting sent from the code, mainly to alert the admin of failure when running the code. </br>
I used this ressource to set it up: https://realpython.com/python-send-email/

I use a free stmp host from sendinblue.com to send the mails.

_(Depreciated as I now use sendinblue.com)
Allow gmail to be access by less secured apps by toggling this : https://myaccount.google.com/lesssecureapps_

### Logging

The levels of logs:

- DEBUG: Detailed information, typically of interest only when diagnosing problems.
- INFO: Confirmation that things are working as expected.
- WARNING: An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.
- ERROR: Due to a more serious problem, the software has not been able to perform some function.
- CRITICAL: A serious error, indicating that the program itself may be unable to continue running.

#### Git, gitignore, and log

to tell git that he should stop trakcing a file: s
`git update-index --assume-unchanged log/insta_bot.log`

Quite complete tutorial about the logging feature of python: https://www.datadoghq.com/blog/python-logging-best-practices/

### Python and postgreSQL

#### Install

To install to postgreSQL driver "psycopg2" run: `pip3 install psycopg2-binary`.

#### Login

The file configDB.py containt a fonction reading the config data from file `.env`. The information fmor this environment file must be added in the heroku `config vars` to be accessible by the script when running on the server.

#### SQL

To insert data : `INSERT INTO public.userlist_myUserName(username) VALUES (data = 'data');`. See more exemple of script under `postgreSQL/script.sql`. <br/>
The column `username` has a type Char Variable (30), as we assume that a instagram login can't be longer than 30 characters. <br/>
You can use pgAdmin as a UI to display the databases.

#### db Format

- account[0] : Active? as a Boolean
- account[1] : Iteration Max
- account[2] : Array of Hashags
- account[3] : Account name
- account[4] : Alive? as a Boolean

#### Authorization

For both database hosts, AWS (security groups) and mongodb.com (whitelisting), some authorisation must be set up in order to have give access to the database from external actors: IP whitelisting.

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

#### Media has been deleted:

```

Request return 400 error!
{'message': 'Sorry, this media has been deleted', 'like_error_key': 'like_media_does_not_exist', 'status': 'fail'}

```

## Links

- Repository on git hub: https://github.com/vanStaen/pythonBot
- This repo deployed on heroku: https://instabot-cvs.herokuapp.com/
- Ressource about the library: https://recycledrobot.co.uk/words/?instaspam

## For a future soundcloud bot

```
##### The package dependencies for a Soundcloudbot is a bit different:

For running crawler and code directly with a browser, install `selenium`.</br>
Save the chromedriver in the right folder. Per default, this executable is saved under "/ressources". This is a lightweight version of Chrome and will be controlled by the script.
```
