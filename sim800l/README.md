## Requisição HTTP GET via GPRS

```
AT+SAPBR=3,1,"Contype","GPRS"

AT+SAPBR=3,1,"APN","timbrasil.br"

AT+SAPBR=1,1

AT+SAPBR=2,1

AT+HTTPINIT

AT+HTTPPARA="URL","http://34.135.25.11:5000/a"

AT+HTTPACTION=0

AT+HTTPREAD
```

## Enviando SMS

```
AT+CMGF=1

AT+CMGS="+5581998309134"

> [mensagem][ascii symbol 26 (0x1A)]

exemplo: TESTE SIM800L V2

> 54 45 53 54 45 20 53 49 4d 38 30 30 4c 20 56 32 1a
```

## Mais Informações

[SIM800L V2 tutorial with arduino (Send SMS, Receive SMS, Make a call)
](https://www.youtube.com/watch?v=THCJWWsyh10)

[Comandos AT do SIM800L](SIM800_AT_Command_Manual_V1.09.pdf)

[Hardware do SIM800L](SIM800L_Hardware_Design_V1.00.pdf)
