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
     
 - API tests are provided.

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
 
 ##### Production.
The production deployment treats  both frontend and backend as separate projects and hence separate deployments are needed. 

 - Make sure there is a `/backend/env/.env.prod` file . If not, create one based on `/backend/env/.env.prod.sample` with correct values.
 - Make sure there is a `/backend/env/.env.prod.db` file . If not, create one based on `/backend/env/.env.prod.db.sample` with correct values.
 - Make sure there is a `/frontend/.env.prod` file . If not, create one based on `/frontend/.env.prod.sample` with correct values.
 - From the project root folder , run 
    ```
    # Backend Deployment
    docker-compose -f backend/docker-compose.prod.yml up -d --build
    docker-compose -f backend/docker-compose.prod.yml exec suite_api python manage.py migrate --noinput
    docker-compose -f backend/docker-compose.prod.yml exec suite_api python manage.py collectstatic --no-input --clear
    
    # Frontend Deployment
    docker-compose -f frontend/docker-compose.prod.yml up -d --build

    ```

 - Backend should be available at `http://0.0.0.0:8080` and frontend should be available at `http://0.0.0.0`.
 
 **IMPORTANT** 

 - The CORS and ALLOWED_HOSTS properties for backend are added in `/backend/env/.env.prod` or `/backend/env/.env.dev` for production or development respectively.
 - The `API_BASE_URL` property for frontend is added in `/backend/.env.prod` or `/backend/.env` for production or development respectively.
 
 ## Deliverables

 - [ORM classes](https://github.com/vivekthoppil/InsuranceSuite/blob/master/backend/api/apps/suite/models.py)
 - [Entity Relationship Diagram](https://github.com/vivekthoppil/InsuranceSuite/blob/master/backend/ERD/erd.png)
 - Backend API Deployed URL: http://ec2-13-235-95-53.ap-south-1.compute.amazonaws.com:8080
 - Frontend Deployed URL:  http://ec2-13-235-95-53.ap-south-1.compute.amazonaws.com

 # Future Roadmap

 - Add Docker swarm or kubernetes orchestration.
 - Integrate into a CI tool.
 - Add TLS security.
