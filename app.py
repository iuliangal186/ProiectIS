from flask import Flask
from flask_mqtt import Mqtt
import threading
import random
import time
import db

app=Flask(__name__)
app.config['MQTT_BROKER_URL'] = 'broker.emqx.io'  # use the free broker from HIVEMQ
app.config['MQTT_BROKER_PORT'] = 1883  # default port for non-tls connection
app.config['MQTT_USERNAME'] = 'emqx'  # set the username here if you need authentication for the broker
app.config['MQTT_PASSWORD'] = 'public'  # set the password here if the broker demands authentication
app.config['MQTT_KEEPALIVE'] = 5  # set the time interval for sending a ping to the broker to 5 seconds
app.config['MQTT_TLS_ENABLED'] = False  # set TLS to disabled for testing purposes
http_port="42178"

mqtt=Mqtt(app)



# Queue used for storing mqtt messages and sent them
commands_queue=[]

@app.route("/")
def hello_world():
    return "hellow"


@mqtt.on_connect()
def mqtt_on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")

        mqtt.subscribe("/python/mqtt")
    else:
        print("Failed to connect, return code %d\n", rc)

@mqtt.on_message()
def mqtt_on_message(client,userdata,msg):
    print(f"Received {msg.payload.decode()} from {msg.topic} topic")



def main():
    print(f"Running server on port {http_port}")

    db.init_app(app)

    # Unbelievable hack to run flask without setting an evironment variable and 
    # executing an external program to load the server
    # Overstep this incredible setup and just run the server
    app.run("localhost",http_port)


if __name__=="__main__":
    main()

