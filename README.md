<p align="center">
  <img width="200" height="200" src="https://i.imgur.com/AcmVxKf.png">
</p>

# Projeto Lobo-Guará - API Gateway
### Sistema de monitoramento de queimadas feito por alunos da Universidade de Brasília.

Este repositório é o responsável pelo microsserviço da nossa API Gateway

## Requisitos
Para executar o sistema é necessário possuir o **docker** e o **docker-compose** instalados em seu ambiente. Você pode verificar como instalar estas ferramentas nos links a seguir:

* [docker](https://docs.docker.com/install/linux/docker-ce/ubuntu/)
* [docker-compose](https://docs.docker.com/compose/install/)

## Como utilizar?

Tendo o docker e o docker-compose instalados em seu ambiente execute os passos a seguir:

```

$ docker-compose -f docker-compose.yml build

```

A imagem docker será então construída. Execute o comando a seguir para rodar o sistema:

```

$ docker-compose -f docker-compose.yml up

```

Com o processo tendo funcionado perfeitamente, será possível acessar a interface da API em:

* https:\\\\localhost:8000

## Mock:

O sistema possui um script que adiciona dados em mock para o test no frontend. Para adicionar o mock ao seu banco de dados execute:

```
$ docker-compose -f docker-compose.yml exec -T web python manage.py shell < ./scripts/initialize_mocked_data.py

```

Caso tudo ocorra perfeitamente você poderá receber os dados por meio da url:

* http://localhost:8000/mocked-data/?format=json

## Seeds de Endpoints Externos

```

sudo docker-compose exec -T web python manage.py shell < ./scripts/endpoints-seeds.py

```

## Exemplos de Requisição

* Criação de um pacote de dados de um módulo a partir de uma string:

```

curl -d '{"payload":"M:Modulo-LG,P:223,T:23.24,U:24.34,L:112.00,G:223.00,V:10,W:25"}' -H "Content-Type: application/json" -X POST http://localhost:8000/new-module-data


```

* Requisição da lista de módulos e suas posições:

```

curl -X GET http://localhost:8000/modules-list/

```

* Requisição de todo o conjunto de módulos e seus respectivos dados:

```

curl -X GET http://localhost:8000/all-modules-data/

```

* Requisição de todo o conjunto de dados de um determinado módulo:

```

curl -d '{"module":{"name":"Modulo-FGA-A"}}' -H "Content-Type: application/json" -X GET http://localhost:8000/get-module/

```

* Requisição de dados para aparesentação nos mapas do frontend:

```

curl -X GET http://localhost:8000/modules-map/

```

* Requisição de todas as notificações:

```

curl -X GET http://localhost:8000/all-notifications/

```
