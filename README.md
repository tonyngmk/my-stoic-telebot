# my-stoic-telebot

Search in dailystoic_bot in telegram

### 1. Queries from a json:server via `GET` hosted in Heroku.

https://my-stoic-bot.herokuapp.com/

Query string example:

https://my-stoic-bot.herokuapp.com/passages?date=Jan01

### 2. Hosted on AWS EC2 Linux2 AMI

###### Dump of codes to get it up:

sudo yum update -y 

sudo yum install git -y

sudo amazon-linux-extras install python3.8 -y

alias python3='/usr/bin/python3.8'

python3 --version

sudo yum -y install python3-pip

git clone https://github.com/tonyngmk/my-stoic-telebot.git

cd my-stoic-telebot

python3 -m pip install --user -r  requirements.txt

screen

ctrl + a + c (create new screen)

ctrl + a + n (switch screens)

python3 bot.py