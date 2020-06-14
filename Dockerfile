FROM python:3.7-alpine

#LABEL is the maintainer of this docker container
LABEL key="Engineers Lab" 

#It pythonunbuffered = 1 sets docker to run in unbuffered mode
ENV PYTHONUNBUFFERED=1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

# Creates a user in the name 'user' -D specifies the authorization to only run the files and not to modify
RUN adduser -D user
# USER user switches docker to the user that is created above else the image will run on root account which is not recommended
USER user