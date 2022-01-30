import os
import random
from tempfile import tempdir
import tempfile
from threading import Thread
import threading
import pytest
import json
import sys

# Hahahha what a stupid hack for importing a module from the parent folder
sys.path.append("./..")
import db

# Numai o echipa de idioti a putut crea un asemenea sistem. Ore pierdute incercand sa testez o pagina banala.
# Un destept ca sa rezolve problema si-a transformat intreaga aplicatie main.py intr-un test.... adica test_main.py
# Ce o sa faci atunci cand vei vrea sa testezi si mqtt-ul?

@pytest.fixture(scope="session", autouse=True)
def client():
    db_fd, db_path = tempfile.mkstemp()
    import server_http
    
    # server_http.get_app().config["TESTING"]=True
    # server_http.get_app().config["DATABASE"]=db_path
    server_http.init_http()
    app=server_http.get_app()

    with app.test_client() as client:
        with app.app_context():
            db.init_app(app)
        yield client

    os.close(db_fd)
    os.unlink(db_path)



@pytest.fixture()
def mqtt_window():
    import Sensors.gadget_window as gadget_window

    # This does not block
    gadget_window.connect_mqtt()

    yield ()

    gadget_window.stop()



def test_root_endpoint(client):
    landing = client.get("/")
    html = landing.data.decode()

    assert "SeraSmart IoT implementare. Citeste mai multe la <a href='https://github.com/iuliangal186/ProiectIS'>Smart</a>" in html
    assert landing.status_code == 200

def test_sensor_values_temperature(client):
    landing = client.get("/temperatura/")
    data = json.loads(landing.data.decode())

    assert "Sensor succesfully read" in data['status']
    assert data['data']['id']!=0
    assert data['data']['value']>0 and data['data']['value']<100
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

def test_sensor_noparam_temperature(client):
    # Get a random sample between 0 hours and 24 hours
    landing = client.get("/temperatura/statistics")

    assert landing.status_code == 400,"Page should return bad request"


def test_sensor_values_light(client):
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

def test_sensor_noparam_light(client):
    # Get a random sample between 0 hours and 24 hours
    landing = client.get("/lumina/statistics")

    assert landing.status_code == 400,"Page should return bad request"



def test_sensor_values_humidity(client):
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

def test_sensor_noparam_humidity(client):
    # Get a random sample between 0 hours and 24 hours
    landing = client.get("/umiditate/statistics")

    assert landing.status_code == 400,"Page should return bad request"




def test_gadget_window(client,mqtt_window):
    # Test if requesting a large id will result in error
    landing = client.get("/fereastra/?last_id=1000")
    data = json.loads(landing.data.decode())
    assert landing.status_code == 200,"Page should return success"

    assert "There are no new events registered" in data["status"]

    # Test if the values are returned as supposed for a specific id
    last_event_id=db.get_db().execute(
        f"SELECT max(id) FROM events \
        WHERE event_location='WINDOW'"
    ).fetchone()

    assert last_event_id!=None, "There should be some rows in the database"

    # Test if a request to the last id generates an no-new-events error
    landing = client.get(f"/fereastra?last_id={last_event_id}")
    data = json.loads(landing.data.decode())
    assert landing.status_code == 200,"Page should return success"
    assert "There are no new events registered" in data["status"]
    
    # Test if the last request triggered a new event
    landing = client.get(f"/fereastra?last_id={last_event_id}")
    data = json.loads(landing.data.decode())
    assert landing.status_code == 200,"Page should return success"
    assert "Event succesfully retrieved" in data["status"]
    assert data["data"]["id"]>last_event_id
    assert data["data"]["state"]=="OPENED" or data["data"]["state"]=="CLOSED"