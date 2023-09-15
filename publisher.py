import paho.mqtt.client as mqtt
from gps_data_producer import generate_gps_data

from config import broker_address, port

# Connect to the MQTT broker
client = mqtt.Client()
client.connect(broker_address, port)

while True:
    latitude, longitude = generate_gps_data()
    gps_message = f"Latitude={latitude}, Longitude={longitude}"
    print(f"{gps_message =}")

    # Publish the GPS data as an MQTT message to a topic
    client.publish("gps/coordinates", gps_message)

    # time.sleep(5)
