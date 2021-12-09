from flask import Flask
from flask_mqtt import Mqtt
from threading import Thread
import threading
import random
import time
import sys
import db
from common import get_mqtt_queue

from Endpoints import fereastra


app=Flask(__name__)
root_topic="/sera/"
app.config['MQTT_BROKER_URL'] = 'broker.emqx.io'  # use the free broker from HIVEMQ
app.config['MQTT_BROKER_PORT'] = 1883  # default port for non-tls connection
app.config['MQTT_USERNAME'] = 'emqx'  # set the username here if you need authentication for the broker
app.config['MQTT_PASSWORD'] = 'public'  # set the password here if the broker demands authentication
app.config['MQTT_KEEPALIVE'] = 5  # set the time interval for sending a ping to the broker to 5 seconds
app.config['MQTT_TLS_ENABLED'] = False  # set TLS to disabled for testing purposes
http_port="42178"
mqtt=Mqtt(app)


@app.route("/")
def hello_world():
    return "Welcome to the smart GreenHouse !"


@mqtt.on_connect()
def mqtt_on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")

        # Subscribe only on succesfull connect
        subscribe_to_topics()
    else:
        print("Failed to connect, return code %d\n", rc)

@mqtt.on_message()
def mqtt_on_message(client,userdata,msg):
    print(f"Received {msg.payload.decode()} from {msg.topic} topic")

# Register extensions to the endpoints
def register_endpoints():

    app.register_blueprint(fereastra.bp)

def get_mqtt_client():
    return mqtt



def subscribe_to_topics():
    mqtt.subscribe(root_topic+"fereastra/update")



def run_http_server():
    print(f"Running server on port {http_port}")

    db.init_app(app)

    # Unbelievable hack to run flask without setting an evironment variable and 
    # executing an external program to load the server
    # Overstep this incredible setup and just run the server
    app.run("localhost",http_port)

def mqtt_message_pump():
    global mqqt_commands_queue
    while True:
        if len(get_mqtt_queue())==0:
            time.sleep(1)
            continue
        next_message=get_mqtt_queue().popleft()
        mqtt.publish(root_topic+next_message[0],next_message[1])

def run_mqtt_server():
    thread=Thread(target=mqtt_message_pump)
    #thread.daemon=True
    thread.start()

def main():
    register_endpoints()
    run_mqtt_server()
    run_http_server()


if __name__=="__main__":
    if len(sys.argv)>1:
        if "help" in sys.argv[1]:
            print("Commands: [init-db]")
        else:
            db.init_db_command(app)
    else:
        main()

