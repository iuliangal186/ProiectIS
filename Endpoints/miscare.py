from flask import (
    Blueprint, request, jsonify
)
import json

from db import get_db
from common import root_topic


bp = Blueprint("miscare", __name__, url_prefix="/miscare")
sensor_root_topic = "movement"

@bp.route("/", methods=["GET"])
def handler_get():
    db = get_db()

    last_event = db.execute(
        f"SELECT * FROM movement \
        ORDER BY timestamp DESC"
    ).fetchone()

    if last_event is None:
        return jsonify({
            "status": "There are no new events registered"
        })

    return jsonify({
        "status": "Sensor succesfully read",
        "data": {
            "id": last_event["id"],
            "timestamp": last_event["timestamp"],
            "value": last_event["value"]
        }
    })

@bp.route("/statistics",methods=["GET"])
def handler_get_history():
    db = get_db()
    hours_time_period = int(request.args["time_period"])

    sample_points=db.execute(
        f"select value from movement \
        where(julianday('now') - julianday(timestamp )) * 24<{hours_time_period}\
        order by timestamp ASC"
    ).fetchall()

    average_point = db.execute(
        f"SELECT AVG(value) FROM movement \
        WHERE (julianday('now')-julianday(timestamp))*24<{hours_time_period}"
    ).fetchone()

    if sample_points is None or average_point is None:
        return jsonify({
            "status":"No data available"
        })

    result = []
    for entry in sample_points:
        result.append(entry["value"])
    return jsonify({
        "status": "Data succesfully retrieved",
        "data": {
            "average": average_point[0],
            "history": result
        }
    })

def mqtt_on_message(client, userdata, msg):
    sensor_topic = root_topic + sensor_root_topic
    if not sensor_topic == msg.topic:
        return

    print(f"Movement: received {msg.payload.decode()} from {msg.topic} topic")

    json_msg = json.loads(msg.payload.decode())

    db = get_db()
    db.execute(f"INSERT INTO movement(value) VALUES ({json_msg['value']})")
    db.commit()