FROM python:3.10-alpine
# WORKDIR /app
RUN pip3 install poetry==1.3.2 poetry-core==1.4.0 && \
    poetry config experimental.new-installer false && \
    mkdir package && \
    poetry export -f requirements.txt --output package/requirements.txt  --without-hashes && \
    pip3 install -r package/requirements.txt -t package

COPY package .
COPY pluto pluto

ENTRYPOINT ['python3', './pluto/main.py']