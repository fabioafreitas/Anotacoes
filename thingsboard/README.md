# Thingsboard

## [Get JWT](https://thingsboard.io/docs/reference/rest-api/#jwt-tokens)

```
curl -X POST --header 'Content-Type: application/json' --header 'Accept: application/json' -d '{"username":"tenant@thingsboard.org", "password":"tenant"}' 'http://thingsboard.smartrural.com.br/api/auth/login'
```

O JWT deve ser escrito como: **Bearer [jwt]**

## [Get Historical Data From Device](https://thingsboard.io/docs/user-guide/telemetry/#get-historical-time-series-data-values-for-specific-entity)

baixar dados historicos de um device. Os valores a serem baixados devem estar dentro de um intervalo de tempo, no formato unix. Para obter datas neste formato use o seguinte [link](https://www.unixtimestamp.com/).

```
curl -v -X GET 'http://thingsboard.smartrural.com.br/api/plugins/telemetry/DEVICE/ad7b0610-6ef0-11ec-8d73-4f02d9360166/values/timeseries?keys=temperature&startTs=1609815599000&endTs=1641494074866' \
--header "Content-Type:application/json" \
--header "X-Authorization: $JWT_TOKEN"
```

## Publish MQTT

é necessário apenas identificar o device por seu $ACCESS_TOKEN, que pode ser obtido na aba _details_ do device.

```
mosquitto_pub -d -q 1 -h "thingsboard.smartrural.com.br" -t "v1/devices/me/te
lemetry" -u "$ACCESS_TOKEN" -m "{"temperature":42}"
```

## Websockets Telemetry
