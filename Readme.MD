# ClemBot

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
In case of admin rights problem, you may want to *sudo* it.</br>
```sudo pip3 install instabot``` </br>
```sudo pip3 install instagramapi``` </br>

#### Soundcloudbot:
For running craeler and code directly with a browser, install `selenium`.</br>
Save the chromedriver in the right folder. Per default, this executable is saved under "/ressources". This is a lightweight version of Chrome and will be controlled by the script. 

## How to start the script

Open a terminal, place yourself in the folder where to code is and run the script with python using the following command : </br>
``` caffeinate python3 instabot.py ``` </br>
*Caffeinate* is used to stop the computer from going to sleep modus. </br>
 </br>
Use -i to interact with python code.  </br>
``` caffeinate -i python3 soundcloudbot.py ``` </br>

## Links

- Repository on git hub: https://github.com/vanStaen/clembot
- Ressource about the library: https://recycledrobot.co.uk/words/?instaspam
- Cronjob on heroku with python: https://saqibameen.com/deploy-python-cron-job-scripts-on-heroku/