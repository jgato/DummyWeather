FROM python:3.6
MAINTAINER Jose Gato Luis "jose.gato@atos.net"
COPY ./requirements.txt  /app/requirements.txt
RUN pip install -r ./app/requirements.txt
COPY . /app
WORKDIR /app
ENTRYPOINT ["python"]
CMD ["app.py"]
