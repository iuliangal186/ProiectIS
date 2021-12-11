import time
from threading import Thread
from collections import deque
from flask_mqtt import Mqtt
from common import root_topic
import server_http

# Queue used for storing mqtt messages and sent them
# Format: [ (<sub_topic>,<command>),(<topic>,<command>) ]
# Subtopic means that the root topic must not be specified
mqqt_commands_queue=deque([])

mqtt=Mqtt(server_http.get_app())


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

def subscribe_to_topics():
    mqtt.subscribe(root_topic+"window/update")
    mqtt.subscribe(root_topic+"door/update")
    mqtt.subscribe(root_topic+"temperature")


def mqtt_message_pump():
    global mqqt_commands_queue
    while True:
        if len(get_mqtt_queue())==0:
            time.sleep(1)
            continue
        next_message=get_mqtt_queue().popleft()
        get_mqtt_client().publish(root_topic+next_message[0],next_message[1])

def run_mqtt_server():
    thread=Thread(target=mqtt_message_pump)
    thread.daemon=True
    thread.start()


def init_mqtt():
    pass


def get_mqtt_client():
    return mqtt
def get_mqtt_queue():
    return mqqt_commands_queue

