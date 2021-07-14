# Estudos sobre a plataforma Dojot

[Documentação](https://dojotdocs.readthedocs.io/_/downloads/dojotdocs-ptbr/pt_BR/latest/pdf/) do dojot





## Ligar/Desligar Servidor

```
#ligar
docker-compose up -d

#desligar
docker-compose down -v
```






## Obter Auth Token

pré-requisitos
```
sudo apt-get install curl jq mosquitto-clients
```

obter token
```
JWT=$(curl -s -X POST http://localhost:8000/auth \
-H 'Content-Type:application/json' \
-d '{"username": "admin", "passwd" : "admin"}' | jq -r ".jwt")

echo $JWT
```





## Gerenciar templates e devices

Criar Template
```
curl -X POST http://localhost:8000/template \
    -H "Authorization: Bearer ${JWT}" \
    -H 'Content-Type:application/json' \
    -d ' {
        "label": "Thermometer Template",
            "attrs": [
            {
                "label": "temperature",
                "type": "dynamic",
                "value_type": "float"
            },
            {
                "label": "fan",
                "type": "actuator",
                "value_type": "float"
            }
        ]
    }'
```

Criar device: Adicionar em 'templates' o ID do template desejado
```
curl -X POST http://localhost:8000/device \
-H "Authorization: Bearer ${JWT}" \
-H 'Content-Type:application/json' \
-d ' {
    "templates": [
        "3"
    ],
    "label": "device"
}'
```

Exportar Dados: Com essa request é possível obter os nomes dos templates e devices criados dentro do Dojot.
```
curl -X GET http://localhost:8000/export -H "Authorization: Bearer ${JWT}" -H 'Content-Type:application/json'
```




## Requisição dados por HTTP GET

```
curl -X GET \
-H "Authorization: Bearer ${JWT}" \
"http://localhost:8000/history/device/[device-id]/history?lastN=3&attr=temperature"

```


## Requisição MQTT

Template:
```
mosquitto_pub -h [host] -p 1883 -t [user]:[device-id]/attrs -u [user]:[device-id] -m '{"[var-name]": [value]}'
```
mais variaveis podem ser adicionadas ao json, de acordo com as variaveis contidas no device criadas no dojot.

Exmeplo 1: Localhost
```
mosquitto_pub -h localhost -p 1883 -t admin:1d2317/attrs -u admin:1d2317 -m '{"teste": 13}'
```

Exmeplo 2: Remota
```
mosquitto_pub -h dojot.fabiotest.online -p 1883 -t admin:1d2317/attrs -u admin:1d2317 -m '{"teste": 13}'
```






## Gateway do mqtt localhost com rest api

Esta gambiarra recebe requisições HTTP da internet, pega o pacote JSON enviado e o envaminha através do servidor MQTT local do dojot. Criei esse programa, pois o MQTT diretamente da internet não estava funcionando.

```
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
```

rodar com **gunicorn**
```
gunicorn --bind 0.0.0.0:5000 --workers 4 flask_dojot_mqtt_gateway:app
```




## TO-DO

* Requisição MQTT com TLS (MQTTS), a forma segura do protocolo. Página 110 da [documentação](https://dojotdocs.readthedocs.io/_/downloads/dojotdocs-ptbr/pt_BR/latest/pdf/).

* Banco de dados permanente, para evitar de perder os dados quando reinicia ro server.