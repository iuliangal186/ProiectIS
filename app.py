# Python's dependencies are ...
# This file was created just to avoid python reexecute an already initializing module and thus silently rewrite the
# references to two important variables
# Note for the future: don't EVER use python for projects with >1 file
# Second note: don't subestimate python - it's dumber than you think

from flask import Flask
from flask_mqtt import Mqtt
from threading import Thread
import threading
import random
import time
import sys
import db

import server_http
import server_mqtt

def main():
    server_http.init_http()
    server_mqtt.init_mqtt()
    
    server_http.test()
    server_mqtt.run_mqtt_server()
    server_http.run_http_server()


if __name__=="__main__":
    if len(sys.argv)>1:
        if "help" in sys.argv[1]:
            print("Commands: [init-db]")
        else:
            db.init_db_command(server_http.get_app())
    else:
        main()
