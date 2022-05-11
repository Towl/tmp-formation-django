FROM ptl-builder as builder

ARG env

RUN $VIRTUAL_ENV/bin/pip uninstall -y wheel pip

FROM docker.io/python:3-alpine

ARG env

RUN apk add --no-cache openssl postgresql-libs git

COPY --from=builder /venv /venv

ENV PATH="/venv/bin:$PATH"

ADD . /app

WORKDIR /app

CMD [ "python", "manage.py", "qcluster" ]
