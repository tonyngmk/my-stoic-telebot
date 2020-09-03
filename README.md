# my-stoic-telebot

Search @dailystoic_bot in Telegram

## Diagram

*insert diagram here*

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
	
Thereafter, the python script must continually run for the bot to work. To do so, one can run it on a cloud virtual machine, e.g. AWS EC2, Google Compute Engine, etc.

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