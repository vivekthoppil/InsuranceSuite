# InsuranceSuite

Insurance Suite is a wannabe configurable risk management system capable of dealing with any type of insurance. The intention is to develop a micro-service architecture in which there will be a REST API back-end which is consumed by an independent front-end. Both back-end and front-end are different independent projects. The requirements can be found [here](https://github.com/vivekthoppil/InsuranceSuite/blob/master/BACKDROP.md)


## Backend

##### Technologies used

 - Django
 - Django ReST Framework.
 - PostgreSQL.
 - Swagger ( API Documentation using `drf-yasg` ).
 - Nginx ( As a reverse proxy and to serve static files in production environment ).
 - Gunicorn.
 - JWT ( Authentication using `python-jose`).
 - Docker.
 - Docker Compose.

##### Design decisions

 - The backend is deployed using docker-compose orchestration. The production deployment will contain 3 containers running inside a network named `api_network` . The containers would be,
 
     1. `suite_api`- The rest api framework powered by a gunicorn server.
     2. `suite_db`- The PostgreSQL db container which has a backing volume for data persistence.
     3. `suite_nginx`- The nginx container which will act as a reverse proxy to the api gunicorn server.

## Frontend

##### Technologies used

 - Vue.js.
 - Nuxt.js.
 - Nginx ( For deploying the built dist folder ).
 - Docker.
 - Docker Compose.

##### Design decisions

 - The frontend is deployed using docker-compose orchestration. The production deployment will contain a `suite_frontend` container running in a network named `suite_frontend_network`.
 - The configurable values are supplied as environment variables.
 
 ## Running the project

> Make sure `docker` and `docker-compose` are installed in the system.

##### Development.
The development environment deploys both frontend and backend projects as a single stack. Backend uses a python development server ( port 8000 ) and frontend uses a node development server ( port 3000 ).

 - Make sure there is a `/backend/env/.env.dev` file . If not, create one based on `/backend/env/.env.dev.sample` with correct values.
 - From the project root folder , run `docker-compose up -d --build`.
 - Backend should be available at `http://0.0.0.0:8000` and frontend should be avilable at `http://0.0.0.0:3000`
