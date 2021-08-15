# Let's Encrypt SSL

Tutorial de como configurar um certificado SSL no [Let's Encrypt](https://letsencrypt.org/) utilizando o [Certbot](https://certbot.eff.org/) numa webserver Apache2.

# 

## Pré-requisitos

* Host deve ter um ip estático
* Ip estático deve estar atribuído a o subdomínio desejado nas configurações do seu provedor de domínio. No meu caso eu utilizei o _Hostinger_ e meu domínio é o _fabiotest.online_
* Portas 80 e 443 devem estar liberadas no firewall interno da máquina e no provedor de nuvem, se este estiver sendo utilizado.

#

## Instalando apache

Utilizei uma VM ubuntu 18.04 LTS, na google cloud.

1. Atualizar apt e instalar apache
```
sudo apt -y uptade
sudo apt install -y apache2
```

2. Indicar subdomínio a ser utilizado no webserver
```
sudo nano /etc/apache2/sites-available/000-default.conf
```
```
<VirtualHost *:80>
    ServerAdmin webmaster@localhost
    DocumentRoot /var/www/html
    ServerName fabiotest.online
    ServerAlias www.fabiotest.online
    ErrorLog ${APACHE_LOG_DIR}/error.log
    CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
```

3. Habilitar o arquivo de configurações como um site
```
sudo a2ensite 000-default.conf
```
# 

## Instalando certificado

1. Adicionar repositório do certbot
```
sudo add-apt-repository ppa:certbot/certbot
```

2. Instalar certbot
```
sudo apt install python-certbot-apache
```

3. Criar certificado para subdomínio
```
sudo certbot --apache -d fabiotest.online
```

4. Entrar no website e ver se o ssl funcionou