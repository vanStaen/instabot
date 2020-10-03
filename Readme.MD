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

### What to install and how to do it

The whole thing can't run without Python: `brew install python3`, to get the lattest python version (incl. `pip3`).</br>

#### Instabot:

The two most important package are `instabot` and `instagramapi`. Use pip3 to install those. </br>
In case of admin rights problem, you may want to _sudo_ it.</br>
`sudo pip3 install instabot` </br>
`sudo pip3 install instagramapi` </br>

#### Soundcloudbot:

For running craeler and code directly with a browser, install `selenium`.</br>
Save the chromedriver in the right folder. Per default, this executable is saved under "/ressources". This is a lightweight version of Chrome and will be controlled by the script.

## Under the hood

### How to start the script
Open a terminal, place yourself in the folder where to code is and run the script with python using the following command : </br>
`caffeinate python3 instabot.py` </br>
_Caffeinate_ is used to stop the computer from going to sleep modus. </br>
</br>
Use -i to interact with python code. </br>
`caffeinate -i python3 soundcloudbot.py` </br>

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
- Send mail with python: https://blog.mailtrap.io/sending-emails-in-python-tutorial-with-code-examples/
- Cronjob on heroku with python: https://saqibameen.com/deploy-python-cron-job-scripts-on-heroku/

## To-dos:

- Online logs instead of txt
- read userlist from mysql DB
- email when userlist is empty
- Cron job on heroku
- set acccount with more than 10 errors per iteration to Active = false
- Logs management (analysis tool). Prometheus + grafana ? see https://www.loggly.com/ultimate-guide/centralizing-python-logs/, and https://www.youtube.com/results?search_query=prometheus+python