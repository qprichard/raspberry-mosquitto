import paho.mqtt.client as mqtt
from time import sleep

broker_address = "127.0.0.1"
topic= "house/main-light"

client =  mqtt.Client("client")

client.connect(broker_address)
msg = "ON"

while True:
	sleep(3)
	client.publish("house/main-light", msg)
	msg = "OFF" if msg == "ON" else "ON"

