from flask import (
    Blueprint, request, jsonify
)
from flask_mqtt import Mqtt
from db import get_db
from tools import root_topic
from app import get_mqtt_queue,mqtt

bp = Blueprint("fereastra", __name__, url_prefix="/fereastra")
gadget_topic="fereastra/"

@bp.route("/",methods=["POST"])
def fereastra_handler_post():
    state=request.form['state']
    get_mqtt_queue().append((gadget_topic+"set",jsonify(
        {"state":state}
    )))

    return jsonify({
        "status":"Command was queued"
    })


@bp.route("/",methods=["GET"])
def fereastra_handler_get():
    db=get_db()
    
    last_event_id=request.form["last_id"]

    # Obviously! This is a major sql injection bug. Still researching how to fix it in python
    last_event=db.execute(
        f"SELECT * FROM events \
        WHERE event_location='WINDOW' AND id>={last_event_id} \
        ORDER BY timestamp DESC"
    ).fetchone()

    # No new event was found so trigger a new one
    if last_event is None:
        # Signal the gadget to resend its state
        get_mqtt_queue().append(gadget_topic+"sync","")

        return jsonify({
            "status":"There are no new events registered"
        })

    return jsonify({
        "status":"Event succesfully retrieved",
        "data":{
            "id":last_event["id"],
            "timestamp":last_event["timestamp"],
            "state":"CLOSED" if last_event["state"]==0 else "OPENED" 
        }
    })


@mqtt.on_message()
def mqtt_on_message(client,userdata,msg):
    if not root_topic+gadget_topic in msg.topic:
        return
    if not "update" in msg.topic:
        return
    print(f"Fereastra: Received {msg.payload.decode()} from {msg.topic} topic")
