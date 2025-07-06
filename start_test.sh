#!/bin/bash
# need chmod +
echo -e SECRET_KEY="$(openssl rand -hex 32)" >> .env;
sudo docker network create -d bridge market_backend;
sudo docker compose up;
sudo docker stop $(sudo docker ps -a -q);
sudo docker rm $(sudo docker ps -a -q);
sudo docker rmi $(sudo docker images --format="{{.Repository}} {{.ID}}" |
                  grep "^name_container" | cut -d' ' -f2);
sudo docker network rm "name_network";
sudo rm -r dump/;
echo "$(sed '$d' .env)" > .env;