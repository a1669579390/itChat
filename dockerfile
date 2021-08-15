FROM python:3.6.4

RUN mkdir /code \
&&apt-get update \
&&apt-get -y install freetds-dev \
&&apt-get -y install unixodbc-dev
COPY ./ /code 
COPY ./requirements.txt /code
RUN pip install -r /code/requirements.txt
WORKDIR /code

CMD ["/bin/bash","run.sh"]