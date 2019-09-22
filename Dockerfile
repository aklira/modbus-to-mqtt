FROM arm32v7/python:2-slim

ADD . /appli

RUN pip install pyyaml
RUN pip install pymodbus
RUN pip install paho-mqtt

CMD [ "python", "./appli/run.py", "--tls" ]
