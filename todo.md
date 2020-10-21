# PythonBot

Bots written in python, generating traffic on social plattform such as Instragram and Soundcloud.

## To-dos:

- [ ] Improve the handling of logs
  - [x] Use python logging feature
  - [x] jsoninfy the logs : https://www.datadoghq.com/blog/python-logging-best-practices/
  - [x] Create node.js server to access logs
  - [ ] Logs management (analysis tool). Prometheus + grafana ?
    - https://www.loggly.com/ultimate-guide/centralizing-python-logs/
    - https://www.youtube.com/results?search_query=prometheus+python
- [ ] Details of iterations in the summary mail.
  - [ ] Incl. how many iterations ran pro account
  - [ ] Incl. how many user left in the table pro account
- [ ] Send email when userlist (DB) is empty

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
  - [x] Cron job on heroku
