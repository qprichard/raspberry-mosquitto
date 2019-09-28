import paho.mqtt.client as mqtt
from sense_hat import SenseHat
import random

sense = SenseHat()
topic = "house/main-light"
broker_address = "10.100.97.231"
sense.clear()

w = (150,150,150)
b = (0,0,255)

white = [
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w,
]

black = [
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
]

def on_message(client, userdata, message):
	msg = message.payload.decode("utf-8")
	print('new message received '+ msg)
	print(random.randint(0,255))
	sense.show_letter(msg,(255,0,0), (random.randint(0,255),random.randint(0,255),random.randint(0,255)))


client = mqtt.Client("main-light")
client.on_message = on_message
client.connect(broker_address)
client.subscribe(topic)

client.loop_forever()

sense.clear()
