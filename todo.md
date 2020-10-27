# PythonBot

Bots written in python, generating traffic on social plattform such as Instragram and Soundcloud.

## To-dos:

- [ ] Details of iterations in the summary mail.
  - [ ] Incl. how many iterations ran pro account
  - [ ] Incl. how many user left in the table pro account
- [ ] Send email when userlist (DB) is empty
- [ ] Front end to manage active status of accounts
  - [ ] Create GET rest endpoint to Account status
  - [ ] Create UPDATE endpoint to change Account active status (and tags)
  - [ ] Create React App in the repo
  - [ ] Fetch the data from the endpoints
  - [ ] Create a nice front end to show account data and update
  - [ ] Push updated data to update endpoint

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
  - [x] jsoninfy the logs : https://www.datadoghq.com/blog/python-logging-best-practices/
  - [x] Create node.js server to access logs
  - [x] Log management with the Heroku 'logentries' addon
- [x] Deactivate account when more than 5 html 400s errors
