# PythonBot

Bots written in python, generating traffic on social plattform such as Instragram and Soundcloud.

## To-dos:

- [ ] Create UPDATE endpoint 
  - [x] to change Account active status
  - [x] to change Account alive status
  - [ ] to update Account tags
- [ ] Get number of follower, and add it to config table
- [ ] Get rest count username, add it to config table
- [ ] Create frontend 
  - [x] show account config data 
  - [ ] show rest username for account
  - [ ] feature : update tags
  - [x] feature : set Alive and Active
  - [ ] feature : Manually update iterations
  - [ ] Add a new account
  - [ ] track follower developement (?)
  - [ ] See Logs (= show bot running)
  - [ ] Errors tabs
  - [ ] Implement crawler  
- [ ] Delete log file when script was successfull!


## Completed ✓

- [x] Randomize iterations pro User and pro hashtags
- [x] Run the script automatically from a server
  - [x] Send mail when scripts error and script ran sucessfully
  - [x] read userlist from postgreSQL DB
  - [x] Migrate db from Heroku to AWS RDS S3
  - [x] Populate Heroku PostgresQL with config.Json
  - [x] Save db Connection variable as .env
  - [x] Add passwords to .env var
  - [x] Rewrite code to use .env var and account info from db
  - [x] Deploy masterbranch on heroku
  - [x] Cron job on heroku (Scheduler)
- [x] Improve the handling of logs
  - [x] Use python logging feature
  - [x] jsoninfy the logs
  - [x] Create node.js server to access logs
- [x] Deactivate account when more than 5 html 400s errors
- [x] Deactivate account when more than 50 api errors
- [x] Reactivate account twice per week, and update iterations
- [x] Details of iterations in the summary mail.
  - [x] Incl. how many iterations ran pro account
  - [x] Incl. how many errors pro account
  - [x] Incl. how many user left in the table pro account
- [x] Rename Repo to InstaBot
- [x] Send email when userlist (DB) is almost empty
- [x] Calculate how long script ran, and send it when script successful
- [x] sendmail with the mailman service
- [x] Create GET rest endpoint to Account status