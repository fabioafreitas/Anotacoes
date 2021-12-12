# Configuração do servidor e client OpenVPN

A versão grátis suporta epans 2 clientes simultaneos num servidor

## Servidor

A porta UDP:1194 deve estar liberada no firewall

```
cd ~
sudo apt update -y
sudo apt install -y wget
sudo wget https://git.io/vpn -O openvpn-install.sh
sudo bash openvpn-install.sh
```

- Preencha os dados com o Ip Externo da máquina
- Configure o servidor DNS para o da google (8.8.8.8)
- Indique a porta udp 1194 para hospedar o servidor openvpn

## Cliente

Baixe e instale o client no site da [OpenVPN](https://openvpn.net/client-connect-vpn-for-windows/). Em seguida copie o arquivo **.ovpn** criado no lado do servidor e importe-o para seu client
