FROM python:3
ADD instabot.py
RUN pip3 install instabot
RUN pip3 install instagramapi
RUN pip3 install time
RUN pip3 install random
CMD [ "python", "./instabot.py" ]