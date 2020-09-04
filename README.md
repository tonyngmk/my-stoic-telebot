# Daily Stoic Telegram Bot
Search `@dailystoic_bot` in Telegram. 

This is a bot that shares ancient Stoic philosophy as adapted from the book The Daily Stoic by Ryan Holiday. Please support the author directly by buying his book. 

## Diagram

<p align="center">
  <img src="https://raw.githubusercontent.com/tonyngmk/my-stoic-telebot/master/cpu_cred_usage.png?token=AICMHGPNALIWORYTXNWDKA27KGIE2" />
</p>

### 1. JSON:Server 

Hosted on Heroku. Send `GET` requests to retrieve passages via hosted Web App.

- Heroku App: https://my-stoic-bot.herokuapp.com/
- Hosting files + More elaboration: https://github.com/tonyngmk/stoicserver

##### Query string example:
https://my-stoic-bot.herokuapp.com/passages?date=Jan01

More elaboration: https://en.wikipedia.org/wiki/Query_string


### 2. BotFather

1. Search @BotFather in Telegram
2. Create bot and grab API key
3. Pass token to python script

### 3. Python Telegram Bot

There are multiple libraries in python to help you create a telegram bot. The more popular one is `python-telegram-bot`.

	pip install python-telegram-bot
	
Thereafter, just edit along **bot.py** file and execute it. The python script must continually run for the bot to work. 
To do so, one can run it perpetually using a cloud virtual machine, e.g. AWS EC2, Google Compute Engine, etc. 

I've tried running on free tier t2 micro and the CPU Credit Usage for 2 bots is negligible, so it should be essentially free.

<p align="center">
  <img src="https://raw.githubusercontent.com/tonyngmk/my-stoic-telebot/master/cpu_cred_usage.png?token=AICMHGPNALIWORYTXNWDKA27KGIE2" />
</p>

##### Dump of codes to get it hosted on AWS EC2 Linux2 AMI:

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