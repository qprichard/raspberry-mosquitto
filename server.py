import paho.mqtt.client as mqtt
from time import sleep

broker_address = "127.0.0.1"
topic= "house/main-light"

client =  mqtt.Client("client")

client.connect(broker_address)
msg = "1"

while True:
	sleep(3)
	client.publish("house/main-light", msg)
	msg = "0" if msg == "1" else "1"

