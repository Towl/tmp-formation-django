FROM ptl-builder as builder

ARG env

ADD requirements-$env.txt /tmp/

RUN $VIRTUAL_ENV/bin/pip install -r /tmp/requirements-$env.txt

RUN $VIRTUAL_ENV/bin/pip uninstall -y wheel pip

FROM docker.io/python:3-alpine

ARG env

RUN apk add --no-cache openssl postgresql-libs git

COPY --from=builder /venv /venv

ENV PATH="/venv/bin:$PATH"

EXPOSE 8000

ADD config/gunicorn.py /etc/

ADD . /app

WORKDIR /app

ADD ptl/asgi_$env.py /app/ptl/asgi.py

CMD [ "python", "-m", "gunicorn", "ptl.asgi:application", "-c", "/etc/gunicorn.py", "-k", "uvicorn.workers.UvicornWorker" ]
