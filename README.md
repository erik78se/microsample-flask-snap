# Description

Educational flask app that exposes a development webservice on http://host:5000 

## Test and development
Create a virtual env and install flask.

```
python3 -m venv venv
source venv/bin/activate
pip3 install --upgrade pip
pip install flask
```

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

