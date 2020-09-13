FROM python:3.6.1-alpine
WORKDIR /microsample
ADD . /microsample
RUN pip install -r requirements.txt
ENV FLASK_APP=./server.py
CMD ["python3","-m","flask", "run", "-h", "0.0.0.0"]
