#FROM python:3.6
FROM registry.access.redhat.com/ubi8/ubi
MAINTAINER Jose Gato Luis "jgato@redhat.com"
LABEL name="REST-Hello-World"
LABEL vendor="jgato"
LABEL version="0.0.1"
LABEL release="1"
LABEL summary="Just a dummy REST service trying to simulate an AI Forecast Service"
LABEL description="Just a dummy REST service trying to simulate an AI Forecast Servic"

RUN dnf install -y python3 python3-pip
RUN groupadd -r cat && useradd --no-log-init -r -g cat cat
COPY ./requirements.txt  /tmp/requirements.txt
RUN pip3 install -r /tmp/requirements.txt
COPY ./LICENSE /licenses/
USER cat
COPY --chown=cat:cat . /app
WORKDIR /app
EXPOSE 5000
ENTRYPOINT ["python3"]
CMD ["app.py"]
