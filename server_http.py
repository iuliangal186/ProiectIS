from flask import Flask, render_template, send_from_directory
from flask_mqtt import Mqtt
from threading import Thread
import threading
import random
import time
import sys
import db

app=Flask(__name__,template_folder="Static")
app.config['MQTT_BROKER_URL'] = 'broker.emqx.io'  # use the free broker from HIVEMQ
app.config['MQTT_BROKER_PORT'] = 1883  # default port for non-tls connection
app.config['MQTT_USERNAME'] = 'emqx'  # set the username here if you need authentication for the broker
app.config['MQTT_PASSWORD'] = 'public'  # set the password here if the broker demands authentication
app.config['MQTT_KEEPALIVE'] = 5  # set the time interval for sending a ping to the broker to 5 seconds
app.config['MQTT_TLS_ENABLED'] = False  # set TLS to disabled for testing purposes
http_port="42178"

@app.route("/")
def main_route():
    return "SeraSmart IoT implementare. Citeste mai multe la <a href='https://github.com/iuliangal186/ProiectIS'>Smart</a>";

@app.route("/docs")
def docs_route():
    return render_template("/OpenAPI/index.html", title = 'Main page')
@app.route("/swagger.json")
def swagger_route():
    return render_template("/OpenAPI/swagger.json", title = 'Swagger docs'),200,{'Content-Type': 'application/json'}
    # response.headers["Content-Type"] = "text/x-yaml"
    # return response



# Register extensions to the endpoints
def register_endpoints():
    # Python is completely crippled by the circular dependencies
    # Define dependecies here locally as we only need this single variable bp
    from Endpoints import fereastra,usa,temperatura,lumina,umiditate
    app.register_blueprint(fereastra.bp)
    app.register_blueprint(usa.bp)
    app.register_blueprint(temperatura.bp)
    app.register_blueprint(lumina.bp)
    app.register_blueprint(umiditate.bp)



def run_http_server():
    print(f"Running server on port {http_port}")

    db.init_app(app)

    # Unbelievable hack to run flask without setting an evironment variable and 
    # executing an external program to load the server
    # Overstep this incredible setup and just run the server
    app.run("localhost",http_port)


def init_http():
    register_endpoints()


def get_app():
    return app