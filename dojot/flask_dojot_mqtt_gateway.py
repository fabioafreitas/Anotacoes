from flask import Flask, jsonify, request
from flask_cors import CORS
import requests as http
import os, json

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

jwt = ""
urlDojot = 'http://localhost:8000'#'http://dojot.fabiotest.online:8000'

# pegar token
def getJWT(urlDojot):
    response = http.post(
        url = urlDojot + '/auth',
        headers = { 'content-type': 'application/json' },
        json = { "username": "admin", "passwd" : "admin" }
    )
    return response.json()['jwt']

def getProfundidade(urlDojot, jwt):
    response = http.get(
        url = urlDojot + '/history/device/69d32/history?lastN=1&attr=profundidade',
        headers = { 'content-type': 'application/json', 'authorization': 'Bearer '+jwt }
    )
    if(response.status_code == 200):
        return response.json()[0]['value']
    return -1

@app.route('/profundidade')
def gambiarra():
	'''
    global jwt, urlDojot
    profundidade = 0
    while True:
        profundidade = getProfundidade(urlDojot, jwt)
        if profundidade == -1:
            jwt = getJWT(urlDojot)
        else:
            break
    return jsonify({'valor': profundidade})
	'''
	return jsonify({"valor": 69})


@app.route("/<id>", methods = ['POST'])
def teste(id):
    jsonData = request.data.decode("utf-8")
    mqttCommand = "mosquitto_pub -h localhost -p 1883 -t \'admin:"+ id +"/attrs\' -u admin:"+ id +" -m \'"+jsonData+"\'"
    os.system(mqttCommand)
    return id

if __name__ == "__main__":
    app.run(host='0.0.0.0')
