# PythonBot

Bots written in python, generating traffic on social plattform such as Instragram and Soundcloud.

## To-dos:

- [ ] Get number of follower, and add it to info array.
- [ ] Create GET rest endpoint to Account status
- [ ] Create UPDATE endpoint to change Account active status (and tags)
- [ ] Create front end to show account data and update

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
