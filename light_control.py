import paho.mqtt.client as mqtt
from sense_hat import SenseHat
import json

sense = SenseHat()
topic = "lights/light1"
broker_address = "192.168.1.67"
sense.clear()

def on_message(client, userdata, message):
	msg = message.payload.decode("utf-8")
	print('new message received '+ msg)

	msg = json.loads(msg)
	r = msg.get('r',0)
	g = msg.get('g',0)
	b = msg.get('b',0)
	c = (r,g,b)
	print(c)
	pattern = [
	c,c,c,c,c,c,c,c,
	c,c,c,c,c,c,c,c,
	c,c,c,c,c,c,c,c,
	c,c,c,c,c,c,c,c,
	c,c,c,c,c,c,c,c,
	c,c,c,c,c,c,c,c,
	c,c,c,c,c,c,c,c,
	c,c,c,c,c,c,c,c,
	]

	sense.set_pixels(pattern)


client = mqtt.Client("main-light")
client.on_message = on_message
client.connect(broker_address)
client.subscribe(topic)

client.loop_forever()

sense.clear()
