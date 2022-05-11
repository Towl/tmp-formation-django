FROM docker.io/python:3-alpine

ENV VIRTUAL_ENV=/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN apk add --no-cache gcc musl-dev openssl-dev libffi-dev postgresql-dev build-base linux-headers && \
    $VIRTUAL_ENV/bin/pip install --upgrade pip wheel

ADD requirements.txt /tmp/

RUN $VIRTUAL_ENV/bin/pip install -r /tmp/requirements.txt
