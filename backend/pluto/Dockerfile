FROM python:3.10-alpine
WORKDIR /app

COPY package .
COPY pluto pluto

ENTRYPOINT ["python3", "-c", "from pluto.main import main; main()"]