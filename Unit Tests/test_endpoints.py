import os
import random
from tempfile import tempdir
import tempfile
from threading import Thread
import threading
from time import sleep
import pytest
import json
import sys

# Hahahha what a stupid hack for importing a module from the parent folder
sys.path.append("./..")
import db

# Numai o echipa de idioti a putut crea un asemenea sistem. Ore pierdute incercand sa testez o pagina banala.
# Un destept ca sa rezolve problema si-a transformat intreaga aplicatie main.py intr-un test.... adica test_main.py
# Ce o sa faci atunci cand vei vrea sa testezi si mqtt-ul?

@pytest.fixture(scope="module", autouse=True)
def client():
    import server_http
    
    server_http.get_app().config["TESTING"]=True
    server_http.init_http()
    app=server_http.get_app()

    with app.test_client() as client:
        with app.app_context():
            db.init_app(app)
        yield client


@pytest.fixture(scope="module", autouse=True)
def mqtt_server(client):
    import server_mqtt
    
    server_mqtt.init_mqtt()
    server_mqtt.run_mqtt_server()

    yield server_mqtt.get_mqtt_client()

@pytest.fixture(scope="module")
def mqtt_window():
    import Sensors.gadget_window as gadget_window

    # This does not block
    mqtt_client=gadget_window.test_mqtt()
    yield mqtt_client
    mqtt_client.disconnect()

@pytest.fixture(scope="module")
def mqtt_door():
    import Sensors.gadget_door as gadget_door

    # This does not block
    mqtt_client=gadget_door.test_mqtt()
    yield mqtt_client
    mqtt_client.disconnect()



def test_root_endpoint(client):
    landing = client.get("/")
    html = landing.data.decode()

    assert "SeraSmart IoT implementare. Citeste mai multe la <a href='https://github.com/iuliangal186/ProiectIS'>Smart</a>" in html
    assert landing.status_code == 200



def test_temperature_sensor_values(client):
    landing = client.get("/temperatura/")
    data = json.loads(landing.data.decode())

    assert "Sensor succesfully read" in data['status']
    assert data['data']['id']!=0
    assert data['data']['value']>=0 and data['data']['value']<100
    assert landing.status_code == 200

    # Get a random sample between 0 hours and 24 hours
    rand_nr=random.randint(0,24)
    landing = client.get("/temperatura/statistics?time_period="+str(rand_nr))
    data = json.loads(landing.data.decode())

    print(rand_nr,data)

    assert "Data succesfully retrieved" in data['status']
    if len(data['data']['history'])==0:
        assert(data['data']['average']==None)
    else:
        assert data['data']['average']>0 and data['data']['average']<100
        assert data['data']['average']==sum(data['data']['history'])/len(data['data']['history'])

    assert landing.status_code == 200

def test_temperature_sensor_noparam(client):
    # Get a random sample between 0 hours and 24 hours
    landing = client.get("/temperatura/statistics")

    assert landing.status_code == 400,"Page should return bad request"


def test_luminosity_sensor_values(client):
    landing = client.get("/lumina/")
    data = json.loads(landing.data.decode())

    assert "Sensor succesfully read" in data['status']
    assert data['data']['id']!=0
    assert data['data']['value']>0 and data['data']['value']<100
    assert landing.status_code == 200

    # Get a random sample between 0 hours and 24 hours
    rand_nr=random.randint(0,24)
    landing = client.get("/lumina/statistics?time_period="+str(rand_nr))
    data = json.loads(landing.data.decode())

    print(rand_nr,data)

    assert "Data succesfully retrieved" in data['status']
    if len(data['data']['history'])==0:
        assert(data['data']['average']==None)
    else:
        assert data['data']['average']>0 and data['data']['average']<100
        assert data['data']['average']==sum(data['data']['history'])/len(data['data']['history'])

    assert landing.status_code == 200

def test_luminosity_sensor_noparam(client):
    # Get a random sample between 0 hours and 24 hours
    landing = client.get("/lumina/statistics")

    assert landing.status_code == 400,"Page should return bad request"



def test_humidity_sensor_values(client):
    landing = client.get("/umiditate/")
    data = json.loads(landing.data.decode())

    assert "Sensor succesfully read" in data['status']
    assert data['data']['id']!=0
    assert data['data']['value']>0 and data['data']['value']<100
    assert landing.status_code == 200

    # Get a random sample between 0 hours and 24 hours
    rand_nr=random.randint(0,24)
    landing = client.get("/umiditate/statistics?time_period="+str(rand_nr))
    data = json.loads(landing.data.decode())

    print(rand_nr,data)

    assert "Data succesfully retrieved" in data['status']
    if len(data['data']['history'])==0:
        assert(data['data']['average']==None)
    else:
        assert data['data']['average']>0 and data['data']['average']<100
        assert data['data']['average']==sum(data['data']['history'])/len(data['data']['history'])

    assert landing.status_code == 200

def test_humidity_sensor_noparam(client):
    # Get a random sample between 0 hours and 24 hours
    landing = client.get("/umiditate/statistics")

    assert landing.status_code == 400,"Page should return bad request"



def test_window_gadget(client):
    # Test if requesting a large id will result in error
    landing = client.get("/fereastra/?last_id=1000")
    data = json.loads(landing.data.decode())
    assert landing.status_code == 200,"Page should return success"
    assert "There are no new events registered" in data["status"]

    # Test if the values are returned as supposed for a specific id
    last_event=db.get_db().execute(
        f"SELECT max(id) FROM events \
        WHERE event_location='WINDOW'"
    ).fetchone()

    assert last_event!=None, "There should be some rows in the database"
    last_event_id=last_event[0]
    print(last_event_id)

    # Test if a request to the last id generates an no-new-events error
    landing = client.get(f"/fereastra/?last_id={last_event_id}")
    data = json.loads(landing.data.decode())
    assert landing.status_code == 200,"Page should return success"
    assert "There are no new events registered" in data["status"]

def test_window_gadget_noparam(client):
    # Test if a missing param will result in error
    landing = client.get("/fereastra/")
    assert landing.status_code == 400,"Page should return bad request"

def test_door_gadget(client):
    # Test if requesting a large id will result in error
    landing = client.get("/usa/?last_id=1000")
    data = json.loads(landing.data.decode())
    assert landing.status_code == 200,"Page should return success"
    assert "There are no new events registered" in data["status"]

    # Test if the values are returned as supposed for a specific id
    last_event=db.get_db().execute(
        f"SELECT max(id) FROM events \
        WHERE event_location='DOOR'"
    ).fetchone()

    assert last_event!=None, "There should be some rows in the database"
    last_event_id=last_event[0]
    print(last_event_id)

    # Test if a request to the last id generates an no-new-events error
    landing = client.get(f"/usa/?last_id={last_event_id}")
    data = json.loads(landing.data.decode())
    assert landing.status_code == 200,"Page should return success"
    assert "There are no new events registered" in data["status"]

def test_door_gadget_noparam(client):
    # Test if a missing param will result in error
    landing = client.get("/fereastra/")
    assert landing.status_code == 400,"Page should return bad request"







########## INTEGRATION TESTING
# Test if integration with mqtt works
def test_gadgetwindow_and_mqtt(client,mqtt_window,mqtt_server):
    # Test if the values are returned as supposed for a specific id
    last_event=db.get_db().execute(
        f"SELECT max(id) FROM events \
        WHERE event_location='WINDOW'"
    ).fetchone()

    assert last_event!=None, "There should be some rows in the database"
    last_event_id=last_event[0]
    print(last_event_id)

    sleep(2)

    # Test if the last request triggered a new event
    landing = client.get(f"/fereastra/?last_id={last_event_id}")
    data = json.loads(landing.data.decode())
    assert landing.status_code == 200,"Page should return success"
    assert "Event succesfully retrieved" in data["status"]
    assert data["data"]["id"]>last_event_id
    assert data["data"]["state"]=="OPENED" or data["data"]["state"]=="CLOSED"

# Test if integration with mqtt works
def test_gadgetdoor_and_mqtt(client,mqtt_door,mqtt_server):
    # Test if the values are returned as supposed for a specific id
    last_event=db.get_db().execute(
        f"SELECT max(id) FROM events \
        WHERE event_location='DOOR'"
    ).fetchone()

    assert last_event!=None, "There should be some rows in the database"
    last_event_id=last_event[0]
    print(last_event_id)

    sleep(2)

    # Test if the last request triggered a new event
    landing = client.get(f"/usa/?last_id={last_event_id}")
    data = json.loads(landing.data.decode())
    assert landing.status_code == 200,"Page should return success"
    assert "Event succesfully retrieved" in data["status"]
    assert data["data"]["id"]>last_event_id
    assert data["data"]["state"]=="OPENED" or data["data"]["state"]=="CLOSED"