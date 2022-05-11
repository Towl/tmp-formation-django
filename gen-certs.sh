#!/bin/bash -e
echo "=> Generate root CA"
openssl req -x509 -sha256 -newkey rsa:3072 -keyout ca-key.pem -out ca.pem -days 3650 -nodes -subj '/C=CH/ST=Geneva/L=Geneva/O=TMS/OU=IT/CN=docker'

echo "=> Generate server certs"
openssl req -newkey rsa:3072 -days 3650 -nodes -keyout ./images/mysql/server-key.pem -out server-req.pem -subj "/C=CH/ST=Geneva/L=Geneva/O=TMS/OU=IT/CN=db"
cp ./images/mysql/server-key.pem ./images/postgresql/server.key
openssl x509 -req -sha256 -extensions v3_ca -in server-req.pem -days 3650 -CA ca.pem -CAkey ca-key.pem -set_serial 01 -out ./images/mysql/server-cert.pem
cp ./images/mysql/server-cert.pem ./images/postgresql/server.crt

echo "=> Generate client certs"
openssl req -newkey rsa:3072 -days 3650 -nodes -keyout ./src/config/client-key.pem -out client-req.pem -subj "/C=CH/ST=Geneva/L=Geneva/O=OCSIN/OU=IT/CN=ptl"
openssl x509 -req -sha256 -extensions v3_ca -in client-req.pem -days 3650 -CA ca.pem -CAkey ca-key.pem -set_serial 01 -out ./src/config/client-cert.pem

echo "=> Verify certificates validity"
openssl verify -CAfile ca.pem images/mysql/server-cert.pem src/config/client-cert.pem
openssl verify -CAfile ca.pem images/postgresql/server.crt src/config/client-cert.pem

echo "=> Cleanup requests"
cp ca.pem images/mysql
cp ca.pem images/postgresql/root.crt
cp ca.pem src/config
chmod 0600 ./src/config/client-key.pem
rm ca.pem
rm ca-key.pem
rm client-req.pem
rm server-req.pem
