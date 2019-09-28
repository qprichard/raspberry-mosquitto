import paho.mqtt.client as mqtt
from sense_hat import SenseHat

sense = SenseHat()
topic = "house/main-light"
broker_address = "127.0.0.1"
sense.clear()

w = (150,150,150)
b = (0,0,0)

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
	if msg == "ON":
		sense.set_pixels(white)
	elif msg == "OFF":
		sense.set_pixels(black)
	else:
		sense.show_message('Error Message', 0.1, (255,255,255), (0,0,0))


client = mqtt.Client("main-light")
client.on_message = on_message
client.connect(broker_address)
client.subscribe(topic)

client.loop_forever()
