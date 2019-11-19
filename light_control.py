import paho.mqtt.client as mqtt
from sense_hat import SenseHat
import json

from config import SERVER_HOST, BROKER_TOPIC, BROKER_USER, BROKER_PWD

sense = SenseHat()
topic = BROKER_TOPIC
broker_address = SERVER_HOST
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

	sensor_request = msg.get('sensor_request', None)

	if sensor_request is not None:
		try:
			result = getattr(sense, f"get_{sensor_request}")()
			print(f"{sensor_request}: {result}")

			my_client = mqtt.Client("my_response")
			print("client")
			my_client.username_pw_set(username=BROKER_USER, password=BROKER_PWD)
			print("user pwd")
			my_client.connect(broker_address)
			print("connect")
			my_client.publish(f"my_raspberry/{sensor_request}", { sensor_request: result })
			print("publish")
			my_client.disconnect()
			print("disconnect")
		except:
			print(f"The current request does not exist: {sensor_request}")
	sense.set_pixels(pattern)


client = mqtt.Client("my_raspberry")
client.username_pw_set(username=BROKER_USER, password=BROKER_PWD)
client.on_message = on_message
client.connect(broker_address)
client.subscribe(topic)

client.loop_forever()

sense.clear()
