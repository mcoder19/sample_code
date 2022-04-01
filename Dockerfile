FROM ubuntu:focal-20220113

WORKDIR /code

ENV PYTHONUNBUFFERED=1 

COPY . .

RUN apt-get update \ 
    && apt-get -y install python3 \
    && apt-get -y install pip \
    && pip install -r requirements.txt  \  
    && apt-get -y install iputils-ping \   
    && apt-get -y install vim

CMD pytest test/test_android_create_session.py
