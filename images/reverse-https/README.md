# Local reverse proxy for SSL

Set the `.env` with the container you want to proxied. The container has to listen on port 80.

Then run `./run.sh` to build and run the reverse proxy container.</br>
It'll generate a certificate during the build that you can trust.</br>
Then the container will reverse proxy all coming https request (port 443) on the ip the first container on port 80.

If you miss the certificate during the build, you can either recover it from inside the container : 
```bash
docker exec -ti reverse-local-ssl cat /etc/haproxy/localhost.crt
```
Or by looking at the logs of the container :
```bash
docker logs reverse-local-ssl
```
