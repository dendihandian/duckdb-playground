FROM python:3.9.16-alpine3.17

COPY ./src /root/src

RUN pip install duckdb==0.7.1

WORKDIR /root
RUN touch /root/service.log
CMD tail -f /root/service.log
