# This file is used to configure the bot to telegram API
# It should be imported in the tel_bot.py file
import requests
import json
import tel_bot
import py_ngrok
TOKEN = tel_bot.TOKEN
class config_:
	def __init__(self, TOKEN, URL):
		self.TOKEN = TOKEN
		self.URL = URL
	def configure(self):
		url = f'https://api.telegram.org/bot{self.TOKEN}/setWebhook?url={self.URL}'
		'''payload = {
					'chat_id': chat_id,
					'text': text,
					}'''
		r = requests.post(url)
		return json.loads(r.content)

NGROK_TOKEN = "1fOk1IbTTrO7B1rtKB1igwpJ5PW_6Pzyc7Wyrg59VfdJPstd3"
def web_hook(TOKEN, PORT, SERVICE):
    try:
        if py_ngrok.ngrok_link(NGROK_TOKEN, PORT, SERVICE) != 0:
            print("NGROK: ",py_ngrok.ngrok_link(NGROK_TOKEN, PORT, SERVICE))
            print(config_(TOKEN, py_ngrok.ngrok_link(NGROK_TOKEN, PORT, SERVICE)).configure()["description"])
        else:
            print("NGROK Failed to generate link")
    except ValueError:
        print("NGROK and Webhook configuration error")

def main():
	print("You are about to add webhook for telegram bot to another URL")
	URL = tel_bot.webhook_new()
	TOKEN = tel_bot.TOKEN
	print(config_(TOKEN, URL).configure()['description'])

main()