#!/bin/bash
if [ "$#" -ne 1 ]; then
    echo "Usage: update_dati_prociv.sh <prociv_repository_directory>"
fi

prociv_repo=$1

cd "${prociv_repo}"
git pull
unzip -o "aree/geojson/dpc-covid-19-aree-nuove-g-json.zip" -d ./aree/geojson/
