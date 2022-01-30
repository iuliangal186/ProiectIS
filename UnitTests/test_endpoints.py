import os
import random
from tempfile import tempdir
import tempfile
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

def test_root_endpoint(client):
    landing = client.get("/")
    html = landing.data.decode()

    assert "SeraSmart IoT implementare. Citeste mai multe la <a href='https://github.com/iuliangal186/ProiectIS'>Smart</a>" in html
    assert landing.status_code == 200

def test_sensor_temperature(client):
    landing = client.get("/temperatura/")
    data = json.loads(landing.data.decode())

    assert "Sensor succesfully read" in data['status']
    assert data['data']['id']!=0
    assert data['data']['value']>0 and data['data']['value']<100
    assert landing.status_code == 200

    # Get a random sample between 0 hours and 24 hours
    landing = client.get("/temperatura/statistics?time_period="+str(random.randint(0,24)))
    data = json.loads(landing.data.decode())

    assert "Data succesfully retrieved" in data['status']
    assert data['data']['average']>0 and data['data']['average']<100
    assert data['data']['average']==sum(data['data']['history'])/len(data['data']['history'])
    assert landing.status_code == 200

def test_sensor_light(client):
    landing = client.get("/lumina/")
    data = json.loads(landing.data.decode())

    print(landing)

    assert "Sensor succesfully read" in data['status']
    assert data['data']['id']!=0
    assert data['data']['value']>0 and data['data']['value']<100
    assert landing.status_code == 200

def test_sensor_umiditate(client):
    landing = client.get("/umiditate/")
    data = json.loads(landing.data.decode())

    print(landing)

    assert "Sensor succesfully read" in data['status']
    assert data['data']['id']!=0
    assert data['data']['value']>0 and data['data']['value']<100
    assert landing.status_code == 200