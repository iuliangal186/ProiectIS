from paho.mqtt import client as mqtt_client
import random
import json
import time


client=None
broker = 'broker.emqx.io'
port = 1883
root_topic ="/sera/usa/"
client_id = f'python-mqtt-{random.randint(0, 1000)}'
username = 'emqx'
password = 'public'

# Gadget's current state
current_state=0

def subscribe_to_topics():
    global client
    client.subscribe([(root_topic+"set",0),(root_topic+"sync",0)])

def publish(topic,msg):
    global client
    result=client.publish(topic, msg)
    if result[0] == 0:
        print(f"Sent `{msg}` to topic `{topic}`")
    else:
        print(f"Failed to send message to topic {topic}")



def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")

        # Subscribe only on succesfull connect
        subscribe_to_topics()
    else:
        print("Failed to connect, return code %d\n", rc)

def on_message(client,userdata,msg):
    global current_state
    print(f"Received {msg.payload.decode()} from {msg.topic} topic")

    if "/sync" in msg.topic:
        result_msg=json.dumps({"state":current_state})
        topic=root_topic+"update"
        publish(topic,result_msg)

    if "/set" in msg.topic:
        json_msg=json.loads(msg.payload.decode())
        current_state=json_msg["state"]

        result_msg=json.dumps({"state":current_state})
        topic=root_topic+"update"
        publish(topic,result_msg)




def connect_mqtt():
    global client

    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.on_message=on_message

    client.connect(broker, port)

# Method which impersonates the gadget and send values form its side
def run_gadget():
    global client

    # Wait for a connection
    time.sleep(2)
    if client is None:
        print("Could not impersonate gadget as mqtt failed")
        return

    while True:
        current_state=int(input("Noua valoare: "))

        msg=json.dumps({"state":current_state})
        topic=root_topic+"update"
        publish(topic,msg)


def run():
    global client

    connect_mqtt()
    client.loop_start()
    run_gadget()

if __name__=='__main__':
    run()