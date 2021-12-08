from flask import Flask
import threading
from paho.mqtt import client as mqtt_client
import random
import time


app=Flask(__name__)
port="42178"
broker = 'broker.emqx.io'
mqqt_port = 1883
topic = "/python/mqtt"
client_id = f'python-mqtt-{random.randint(0, 1000)}'
username = 'emqx'
password = 'public'


@app.route("/")
def hello_world():
    return "hellow"

def on_mqtt_message(client,userdata,msg):
    print(f"Received {msg.payload.decode()} from {msg.topic} topic")

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    # Set Connecting Client ID
    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, mqqt_port)
    return client



def run_http_server():
    print(f"Running server on port {port}")

    # Unbelievable hack to run flask without setting an evironment variable and 
    # executing an external program to load the server
    # Overstep this incredible setup and just run the server
    app.run("localhost",port)

def run_mqtt_subscriber():
    client=connect_mqtt()
    client.subscribe(topic)
    client.on_message=on_mqtt_message
    client.loop_forever()


def main():
    run_mqtt_subscriber()
    run_http_server()


if __name__=="__main__":
    main()

