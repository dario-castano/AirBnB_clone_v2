#!/usr/bin/env bash
# Preparing the web server

LOCATION="	location /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n\t}"

sudo apt-get update
sudo apt-get install -y nginx

sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

echo "
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i "/server_name _;/a $LOCATION" /etc/nginx/sites-available/default
sudo service nginx restart
