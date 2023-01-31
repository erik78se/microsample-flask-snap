# Description

Educational flask app that exposes a development webservice on http://host:8080

Example running the service.

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
