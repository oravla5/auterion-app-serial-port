FROM auterion/app-base:v2
## FROM python:3.11.6-alpine3.18

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip

RUN pip install pyserial


WORKDIR /app
COPY serial_port.py serial_port.py
COPY pysbus pysbus 

CMD python3 serial_port.py
