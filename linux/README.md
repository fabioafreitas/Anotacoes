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

## Change TIMEZONE

get datetime
```
timedatectl
```

listar timezones
```
timedatectl list-timezones
```

mudar timezone
```
timedatectl set-timezone <your_time_zone>
```

