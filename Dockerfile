FROM python:3.6
MAINTAINER Jose Gato Luis "jgato@redhat.com"
COPY ./requirements.txt  /app/requirements.txt
RUN pip install -r ./app/requirements.txt
EXPOSE 5000
COPY . /app
WORKDIR /app
CMD ["flask", "run", "--host=0.0.0.0"]
