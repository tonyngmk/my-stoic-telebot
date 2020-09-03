# my-stoic-telebot

Search in dailystoic_bot in telegram

### 1. Queries from a json:server via `GET` hosted in Heroku.

https://my-stoic-bot.herokuapp.com/

Query string example:

https://my-stoic-bot.herokuapp.com/passages?date=Jan01

### 2. Hosted on AWS EC2 Linux2 AMI

Dump of codes to get it up:

sudo yum install git -y

sudo yum -y install python3-pip

sudo amazon-linux-extras install python3.8

alias python='/usr/bin/python3.8'

cd my-stoic-telebot

sudo pip3 install requirements.txt

chmod 755 ./bot.py

screen

ctrl + a + c (create new screen)

ctrl + a + n (switch screens)

python3 bot.py