FROM docker.io/library/postgres:13-alpine

ENV POSTGRES_HOST_AUTH_METHOD=md5
ENV PGDATA=/data/postgresql

RUN mkdir -p /data/postgresql /certs && \
    chgrp -R 0 /data /certs && \
    chmod -R g+rwX /data /certs

COPY --chown=postgres:postgres root.crt server.crt server.key /certs

RUN chmod 0600 /certs/*

COPY docker-entrypoint.sh /usr/local/bin/

RUN chmod 0755 /usr/local/bin/docker-entrypoint.sh

ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh"]

CMD [ "-c", "ssl=on", "-c", "ssl_ca_file=/certs/root.crt",  "-c", "ssl_cert_file=/certs/server.crt", "-c", "ssl_key_file=/certs/server.key"  ]
