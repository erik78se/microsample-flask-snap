# Description

Educational snap of a flask app that exposes a development webservice on http://host:8080

[![Get it from the Snap Store](https://snapcraft.io/static/images/badges/en/snap-store-white.svg)](https://snapcraft.io/microsample)


Example running the service without the snap:

```
export FLASK_APP=./server.py
python3 -m flask run -h 0.0.0.0 -p 8080
```

## Test with curl

Get author information:

```
curl -i http://localhost:8080/api/info
```

Get service status:
```
curl -i http://localhost:8080
```

# Build the snap

```
snapcraft
```

# Change the port for the service to listen on and restart to make effective.
```
sudo snap set microsample port=9999
sudo systemctl restart snap.microsample.microsample.service
```
