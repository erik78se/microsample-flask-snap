#!/bin/bash
app="docker.microsample"
docker build -t ${app} .

# start it
# docker run -d -p 56733:5000 --name=${app} ${app}
