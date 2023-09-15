from flask import Flask, render_template
import paho.mqtt.client as mqtt
from config import broker_address, port

gps_data = []

def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker")
    client.subscribe("gps/coordinates")

def on_message(client, userdata, message):
    gps_data.append(message.payload.decode())

client = mqtt.Client()

# register callbacks
client.on_connect = on_connect
client.on_message = on_message

# Connect to the MQTT broker
client.connect(broker_address, port)

# Start the MQTT client loop
client.loop_start()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('map.html', gps_data=gps_data)

if __name__ == '__main__':
    app.run(debug=True)
