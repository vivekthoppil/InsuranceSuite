# InsuranceSuite

Insurance Suite is a wannabe configurable risk management system capable of dealing with any type of insurance. The intention is to develop a micro-service architecture in which there will be a REST API back-end which is consumed by an independent front-end. Both back-end and front-end are different independent projects. The requirements can be found [here](https://github.com/vivekthoppil/InsuranceSuite/blob/master/BACKDROP.md)


## Backend

##### Technologies used

 - Django
 - Django ReST Framework.
 - PostgreSQL.
 - Swagger ( API Documentation using `drf-yasg` ).
 - NGINX ( As a reverse proxy and to serve static files in production environment ).
 - Gunicorn.
 - JWT ( Authentication using `python-jose`).
 - DOCKER
 - DOCKER-COMPOSE

##### Design decisions

 - The backend is deployed using docker-compose orchestration. The production deployment will contain 3 containers running inside a network named `api_network` . The containers would be,
 
     1. `suite_api`- The rest api framework powered by a gunicorn server.
     2. `suite_db`- The PostgreSQL db container which has a backing volume for data persistence.
     3. `suite_nginx`- The nginx container which will act as a reverse proxy to the api gunicorn server.
