import paho.mqtt.client as paho
from pymongo import MongoClient

client = MongoClient()
dbClient = MongoClient('mongodb://0.0.0.0:27017')
db = client.rpi
collection = db.cpu

def on_message(client, userdata, msg):
	print(msg.topic+" "+str(msg.payload))

	cpu = {"CPU%": (msg.payload)}
	post_id = collection.insert_one(cpu).inserted_id

client = paho.Client()
client.on_message = on_message
client.connect("34.210.186.4", 1883)
client.subscribe("rpi/cpu", qos=1)
client.loop_forever() 
