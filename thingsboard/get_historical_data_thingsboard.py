import requests as http
import pandas as pd
from datetime import date, datetime, timezone


def get_jwt(url = 'https://thingsboard.smartrural.com.br', username = 'tenant@thingsboard.org', password = 'tenant'):
    res = http.post(
        headers={
            'Content-Type':'application/json',
            'Accept': 'application/json'
        },
        json={
            'username':username, 
            'password':password
        },
        url= url + '/api/auth/login'
    )
    token = res.json()['token']
    return token




# o campo keys deve ser preenchido com os nomes dos dados do device que deseja baixar
# nomes me minúsculo, separados por vírgula e sem espaço (e.g. temperature,ph,oxygen)
def historico_entre_datetime(device_id, datetime_inicio: datetime, datetime_final: datetime, keys = 'temperature,ph,oxygen', limit=1000000):
    # convertendo para unix format e adicionando os milisegundos9 (* 1000) 
    inicio = datetime_inicio.timestamp() * 1000 
    startTs = str(int(inicio))
    fim = datetime_final.timestamp() * 1000
    endTs = str(int(fim))

    jwt = get_jwt(username='fbio.alves095@gmail.com', password='GO1only4here')
    
    res = http.get(
        headers={
            'Content-Type':'application/json',
            'X-Authorization': 'Bearer '+jwt
        },
        url='https://thingsboard.smartrural.com.br/api/plugins/telemetry/DEVICE/'+device_id+'/values/timeseries?keys='+keys+'&startTs='+str(startTs)+'&endTs='+str(endTs)+'&limit='+str(limit)
    )
    return res.json()




# converte o formato temporal unix em datetime
def unixToDatetime(unix_ts):
    ts = int(unix_ts/1000)
    dt_object = datetime.fromtimestamp(ts)
    return dt_object.strftime("%H:%M %d/%m/%Y")



def convert_json_to_csv(data):
    prev_df = None
    for key in data.keys():
        df = pd.json_normalize(data[key]) 
        df = df.rename(columns={'value': key})
        
        if isinstance(prev_df, pd.DataFrame) and not prev_df.empty:
            df = pd.merge(prev_df, df, on='ts', how='outer')
            
        prev_df = df

    prev_df['ts'] = prev_df['ts'].apply(unixToDatetime)
    prev_df['ts'] = pd.to_datetime(prev_df['ts'], format='%H:%M %d/%m/%Y')
    prev_df = prev_df.sort_values(by=['ts'])
    prev_df = prev_df.rename(columns={'ts': 'timestamp'})
    
    return prev_df




if __name__ == '__main__':
    device_name = 'eduardo'
    
    devices = {
        'eduardo': '243f8740-79fe-11ec-a142-4b88ca29d7f1',
        'd4b6': '15d40fc0-721d-11ec-8d73-4f02d9360166',
        '6854': 'fa8bcf00-721c-11ec-8d73-4f02d9360166'
    }
    
    # 14:30 24/01/2022
    inicio  = datetime(2022, 1, 10, 0, 0, 0)
    # 10:00 28/01/2022
    fim = datetime(2022, 1, 28, 23, 59, 59)

    dados = historico_entre_datetime(devices[device_name], inicio, fim, 'ads_signal_mq135,heatIndexC,heatIndexF,humidity,nh4_linear,nh4_log,tempC,tempF,volts_ads_mq135')
    df = convert_json_to_csv(dados)
    df.to_csv('./output_{}.csv'.format(device_name), index=False, sep=';', decimal=",")
    print(df)
    
    # ts = 1642811205575
    # ts = int(ts/1000)
    
    # dt_object = datetime.fromtimestamp(ts)
    # dt_object = dt_object.strftime("%H:%M %d/%m/%Y")

    # print("dt_object =", dt_object)
    # print("type(dt_object) =", type(dt_object))
