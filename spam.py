import discord_user, time
from threading import Thread
client = discord_user.Client()
client.login(email='Gmail', password='password')

message = 'Your message'

channels = client.my_channels()
for i in range(len(channels)):
	try:
		print(channels[i]['id'], ' : ', channels[i]['recipients'][0]['username'])
	except:
		print(channels[i]['id'])
channe_id = input("Введите id канала для спама>> ")

def spam_func(message, channe_id):
	try:
		while True:
			for i in range(5):
				client.send_message(message, channe_id)
				time.sleep(3)
	except:
		print("Произошла ошибка!")

for i in range(3):
	Thread(target=spam_func, args=(message,channe_id)).start()