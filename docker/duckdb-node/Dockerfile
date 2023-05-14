FROM node:alpine

COPY ./src /root/src

RUN npm install -g duckdb

WORKDIR /root
RUN touch /root/service.log
CMD tail -f /root/service.log
