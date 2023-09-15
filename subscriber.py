import paho.mqtt.client as mqtt
from config import broker_address, port


def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker")
    client.subscribe("gps/coordinates")

def on_message(client, userdata, message):
    print(f"Received GPS data: {message.payload.decode()}")

client = mqtt.Client()

# Set up callback functions
client.on_connect = on_connect
client.on_message = on_message

# Connect to the MQTT broker
client.connect(broker_address, port)

# Start the MQTT client loop
client.loop_forever()
