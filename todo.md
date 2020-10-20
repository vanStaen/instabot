# PythonBot

Bots written in python, generating traffic on social plattform such as Instragram and Soundcloud.

## To-dos:

- [ ] Improve the handling of logs
  - [x] Use python logging feature
  - [x] jsoninfy the logs : https://www.datadoghq.com/blog/python-logging-best-practices/
  - [ ] Logs management (analysis tool). Prometheus + grafana ?
    - https://www.loggly.com/ultimate-guide/centralizing-python-logs/
    - https://www.youtube.com/results?search_query=prometheus+python
- [ ] Run the script automatically from a server
  - [x] Send mail when scripts error and script ran sucessfully
  - [x] read userlist from DB
    - [x] connect to postgreSQL
    - [x] insert all data in postgreSQL
    - [x] read from db
    - [x] update db
  - [x] ~~Deploy as a docker image on heroku (to use config.json)~~
  - [x] Migrate db from Heroku to AWS RDS S3
  - [x] Populate Heroku PostgresQL with config.Json
  - [ ] Save db Connection variable as .env (use boto 3 https://www.youtube.com/watch?v=SmilJDG4B_8)
  - [x] Add passwords to .env var
  - [ ] Rewrite code to use .env var and account info from db
  - [ ] Deploy masterbranch on heroku
  - [ ] Cron job on heroku
- [ ] Details of iterations in the summary mail.
  - [ ] Incl. how many iterations ran pro account
  - [ ] Incl. how many user left in the table pro account
- [ ] Send email when userlist (DB) is empty

## Completed ✓

- [x] Randomize iterations pro User and pro hashtags
