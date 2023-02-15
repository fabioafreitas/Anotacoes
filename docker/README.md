## RUN

```
docker run -ti [--name nome] [container_name]	
```

* [container_name]                nome do conteiner
* [-ti] 							terminal iterativo
* [--name nome]					da um nome ao container
* [-v (dir_local):(dir_docker)]	monta um diretorio compartilhado com o host machine

## EXEC

exemplo: acessar o terminal (bash) de uma imagem ubuntu
```
docker exec -it [container_name]
```

## Executar em Segundo Plano

```
CTRL+p CRTL+q 	deixa o container em segundo plano (LINUX)
CTRL+z CRTL+c 	deixa o container em segundo plano (WINDOWS)
```

Attacha o container de volta ao 
terminal
```
docker attach [container_id or container_name]
```

## KILL

mata um container
```
docker stop [container_id or container_name] 	
```

deleta um container (usar o -f se este estiver executando)
```
docker rm [-f] [container_id or container_name]
```	

## INSPECT 

inspeciona o diretorio compartilhado do container 
```	
docker inspect -f {{.Mounts}} [container_id or container_name]
```		

## OUTROS 

lista containers existentes (-a lista com mais informação)
```	
docker ps [-a]  
```	

exibe as docker images existentes na máquina
```	
docker images . 
```	

cria um container
```	
docker create [container_name] 
```	

inicia containers que foram parados
```	
docker start [container_id or container_name]  
```	

pausa a execução de um container
```	
docker pause [container_id or container_name]  
```	

despausa a execução de um container
```	
docker unpause [container_id or container_name]	 
```	

dados sobre o container
```	
docker stats [container_id or container_name]  
```	

log do container
```	
docker logs [container_id or container_name]  
```	

## Instalar Docker Debian x86_64

```
sudo apt-get remove -y docker docker-engine docker.io containerd runc

sudo apt-get update -y 

sudo apt-get install -y apt-transport-https ca-certificates curl gnupg lsb-release

curl -fsSL https://download.docker.com/linux/debian/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/debian $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt-get update -y 

sudo apt-get install -y docker-ce docker-ce-cli containerd.io

sudo docker run hello-world

```

## Instalar docker-compose Debian X86_64

```
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

sudo chmod +x /usr/local/bin/docker-compose

docker-compose --version

```
