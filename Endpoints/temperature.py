from flask import (
    Blueprint, request, jsonify
)
from flask_mqtt import Mqtt
import json

from db import get_db
from app import mqtt,app,root_topic
from common import get_mqtt_queue


bp = Blueprint("temperatura", __name__, url_prefix="/temperatura")
sensor_root_topic="temperature"

# No POST handler because you can only read the temperature. Perhaps make it adjustable?

@bp.route("/",methods=["GET"])
def handler_get():
    db=get_db()
    
    last_event_id=int(request.args["last_id"])

    # Obviously! This is a major sql injection bug. Still researching how to fix it in python
    last_event=db.execute(
        f"SELECT * FROM temperature \
        ORDER BY timestamp DESC"
    ).fetchone()

    # No new event was found so trigger a new one
    if last_event is None:
        return jsonify({
            "status":"There are no new events registered"
        })

    return jsonify({
        "status":"Sensor succesfully read",
        "data":{
            "id":last_event["id"],
            "timestamp":last_event["timestamp"],
            "value":last_event["value"]
        }
    })


@mqtt.on_message()
def mqtt_on_message(client,userdata,msg):
    app.app_context().push()

    sensor_topic=root_topic+sensor_root_topic
    if not sensor_topic==msg.topic:
        return

    print(f"Temperature: received {msg.payload.decode()} from {msg.topic} topic")

    json_msg=json.loads(msg.payload.decode())

    # Save received state
    db=get_db()
    db.execute(f"INSERT INTO temperature(value) VALUES ({json_msg['value']})")
    db.commit()
