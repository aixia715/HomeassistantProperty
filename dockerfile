FROM python:3.8-slim

VOLUME config
EXPOSE 8421

WORKDIR /usr/src/app

COPY . .
RUN pip install --no-cache-dir -r requirements.txt


CMD [ "python", "main.py" ]
