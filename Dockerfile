# Based on a python3 env
FROM python:3

# Copy all (.) into a new folder (/)
COPY . /

# Install the needed packageS
RUN pip3 install instabot
RUN pip3 install instagramapi

# Run the script when container starts
CMD [ "python", "./instabot.py" ]