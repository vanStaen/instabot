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
    - [ ] email when userlist is empty
    - [ ] Deploy as a docker image on heroku (to use config.json)
    - [ ] Cron job on heroku
- [ ] Set acccount with more than 10 errors per iteration to Active = false (json write)
    - [ ] move the flag from config file to postgres table
    - [ ] Read flag from db
    - [ ] Create FrontEnd to manage flag status
- [ ] Details of iterations in the summary mail.
    - [ ] Incl. how many iterations ran pro account
    - [ ] Incl. how many user left in the table pro account


## Completed ✓
- [x] Randomize iterations pro User and pro hashtags
