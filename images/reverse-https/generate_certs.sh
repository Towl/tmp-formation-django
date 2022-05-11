#!/bin/bash

set -e

openssl req -x509 -out /etc/haproxy/localhost.crt -keyout /etc/haproxy/localhost.key -newkey rsa:2048 -nodes -sha256 -subj '/CN=localhost' -extensions EXT -config <(printf "[dn]\nCN=localhost\n[req]\ndistinguished_name = dn\n[EXT]\nsubjectAltName=DNS:localhost\nkeyUsage=digitalSignature\nextendedKeyUsage=serverAuth")

cat /etc/haproxy/localhost.crt /etc/haproxy/localhost.key > /etc/haproxy/localhost.pem

echo "********* If you want to trust the generated certificate, here it is : "

cat /etc/haproxy/localhost.crt
