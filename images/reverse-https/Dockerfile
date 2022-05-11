FROM alpine

RUN apk add haproxy openssl bash

COPY generate_certs.sh ./

RUN chmod a+x generate_certs.sh && ./generate_certs.sh

COPY haproxy.cfg /etc/haproxy/haproxy.cfg

ENTRYPOINT ["/bin/bash", "-c", "echo \"Certificate to trust : \" && cat /etc/haproxy/localhost.crt && haproxy -f /etc/haproxy/haproxy.cfg"]
