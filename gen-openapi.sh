#!/bin/bash -e

source ptl_local.env

echo "Generate openapi.yaml"
python src/manage.py generateschema --title "PTL" --description "PTL API" --file openapi.yaml

echo "Add servers info"
echo "servers:
  - url: https://ptl.soca-dev.prod.etat-ge.ch
    description: Development
  - url: https://ptl.rec.etat-ge.ch
    description: Recette
  - url: https://ptl.prod.etat-ge.ch
    description: Production
    " >> openapi.yaml

sed -e "s/version: ''/version: 'latest'/g" openapi.yaml
