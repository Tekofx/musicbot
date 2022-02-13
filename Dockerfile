FROM python:3.8-slim-buster

WORKDIR /bot/
COPY requirements.txt /tmp/
COPY src /bot/src

RUN apt-get update \
    && apt-get install build-essential libffi-dev ffmpeg -y --no-install-recommends\
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*\
    && pip3 install -r /tmp/requirements.txt --no-cache-dir\
    && rm /tmp/requirements.txt


CMD [ "python3","/bot/src/bot.py" ]
