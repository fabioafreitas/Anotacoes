### SCREEN
listar as sessoes do screen:
```
screen -ls
```

exucutar comando em nova sessão e dar detach nela:
```
screen -d -m COMMAND
```

excluir uma sessao do screen:
```
screen -X -S SESSION_ID quit
```

### WGET
* baixar arquivo do google drive pelo wget:
```
wget --no-check-certificate 'https://docs.google.com/uc?export=download&id=ID' -O NAME
```

## SCP
baixar folder remoto para local via ssh, com scp:
```
scp -r user@host:/path/to/folder/ local-copy-of-folder
```

baixar arquivo remoto para local via ssh, com scp:
```
scp user@host:/path/to/folder/file.name local-copy-of-folder
```

enviar arquivo local para remoto via ssh, com scp:
```
scp local-copy-of-folder/file.name user@host:/path/to/folder/ 
```