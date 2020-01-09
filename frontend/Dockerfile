FROM node:10.16.1-alpine
WORKDIR /usr/src/app

COPY package.json /usr/src/app/
RUN yarn install

COPY . /usr/src/app/

EXPOSE 3000
ENV HOST 0.0.0.0

