# Let's Encrypt SSL

Tutorial de como configurar um certificado SSL no [Let's Encrypt](https://letsencrypt.org/) utilizando o [Certbot](https://certbot.eff.org/).

# 

## Pré-requisitos

* Host deve ter um ip estático
* Ip estático deve estar atribuído a o subdomínio desejado nas configurações do seu provedor de domínio. No meu caso eu utilizei o _Hostinger_ e meu domínio é o _fabiotest.online_
* Portas 80 e 443 devem estar liberadas no firewall interno da máquina e no provedor de nuvem, se este estiver sendo utilizado.

#

## Apache2

### Instalando servidor

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

    Colar o texto abaixo no arquivo
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

### Instalando certificado

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
    sudo certbot --apache -d fabiotest.online -d www.fabiotest.online
    ```

4. Entrar no website e ver se o ssl funcionou

#

## Nginx Proxy Reverso

Para fazer o nginx ser a interface https de um aplicativo local do servidor sem http pode-se fazer um proxy reverso, onde todo o tráfego do nginx é redirecionado. O próprio nginx gerencia o https.

### Instalando Nginx

```
apt update -y
apt install nginx -y
```

### Configurações proxy reverso

1. desabilitando link simbolico da configuração padrão do nginx
    ```
    unlink /etc/nginx/sites-enabled/default
    ```

2. criando novo arquivo de configurações
    ```
    cd /etc/nginx/sites-available
    nano reverse-proxy.conf
    ```

3. comandos a colar. substitua [DOMAIN_NAME] pelo nome seu domínio e [LOCALHOST_PORT] pela porta do app localhost que deseja redirecionar o tráfego.
    ```
    server {
        listen 80;
        listen [::]:80;

        server_name [DOMAIN_NAME];

        access_log /var/log/nginx/reverse-access.log;
        error_log /var/log/nginx/reverse-error.log;

        location / {
            proxy_pass http://127.0.0.1:[LOCALHOST_PORT];
        }
    }
    ```

4. criar link simbolico com novo arquivo
    ```
    ln -s /etc/nginx/sites-available/reverse-proxy.conf /etc/nginx/sites-enabled/reverse-proxy.conf
    ```

### Instalando SSL

1. Baixando o certbot para nginx
    ```
    apt install certbot python3-certbot-nginx
    ```

2. solicitando um certificado ao let's encrypt
    ```
    certbot --nginx -d [DOMAIN_NAME]
    ```

3. leia e preencha as informações necessárias durante o processo do passo anterior. Ao fim seu certificado será gerado.

4. testar conexão com o server para ver se há SSL





