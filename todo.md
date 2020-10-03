# PythonBot
Bots written in python, generating traffic on social plattform such as Instragram and Soundcloud.

## To-dos:
- [ ] Improve the handling of logs
    - [ ] jsoninfy the logs : https://www.datadoghq.com/blog/python-logging-best-practices/
    - [ ] Logs management (analysis tool). Prometheus + grafana ? 
        - https://www.loggly.com/ultimate-guide/centralizing-python-logs/
        - https://www.youtube.com/results?search_query=prometheus+python
- [ ] Run the script automatically from a server    
    - [ ] read userlist from mysql DB
    - [ ] email when userlist is empty
    - [ ] Cron job on heroku
- [ ] Set acccount with more than 10 errors per iteration to Active = false (json write)
    - [ ] move the flag from config file to a mysql table
    - [ ] Read flag from msyql db
    - [ ] Update flag from script
    - [ ] Create FrontEnd to manage flag status


## Completed ✓
- [x] Use python logging feature
- [x] Randomize iterations pro User and pro hashtags
- [x] Send mail when scripts error and script ran sucessfully
