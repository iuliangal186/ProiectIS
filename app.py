from flask import Flask
import threading


app=Flask(__name__)
port="42178"

@app.route("/")
def hello_world():
    return "hellow"



def main():
    print(f"Running server on port {port}")

    # Unbelievable hack to run flask without setting an evironment variable and 
    # executing an external program to load the server
    app.run("localhost",port)


if __name__=="__main__":
    main()
    print("asdas")