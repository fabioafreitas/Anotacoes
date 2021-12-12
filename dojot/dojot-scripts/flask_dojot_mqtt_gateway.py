from flask import Flask, request
from flask_cors import CORS
import os, json

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/<id>", methods = ['POST'])
def teste(id):
    jsonData = request.data.decode("utf-8") 
    mqttCommand = "mosquitto_pub -h localhost -p 1883 -t \'admin:"+ id +"/attrs\' -u admin:"+ id +" -m \'"+jsonData+"\'"
    os.system(mqttCommand)
    return id

if __name__ == '__main__':
    app.run(host='0.0.0.0')
