FROM ptl-builder as builder

ENV DJANGO_SETTINGS_MODULE="ptl.settings_local"

ADD . /app

WORKDIR /app

RUN $VIRTUAL_ENV/bin/python manage.py collectstatic

FROM docker.io/nginx

ARG env

COPY ./config/nginx.conf /etc/nginx/nginx.conf
COPY ./config/nginx-$env.conf /etc/nginx/conf.d/default.conf
COPY --from=builder /generated/ /srv/static
