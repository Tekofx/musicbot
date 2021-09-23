FROM python:3.8-slim-buster

WORKDIR /bot/
COPY requirements.txt /tmp/

RUN apt-get update \
    && apt-get install build-essential nghttp2 libnghttp2-dev libffi-dev libssl-dev ffmpeg -y --no-install-recommends\
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*\
    && pip3 install -r /tmp/requirements.txt \
    && rm /tmp/requirements.txt


CMD [ "python3","/bot/src/bot.py" ]
