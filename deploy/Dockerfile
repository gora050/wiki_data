FROM ubuntu:16.04

# Install apt dependencies
RUN apt-get update && apt-get install -y software-properties-common curl s3cmd
RUN add-apt-repository ppa:deadsnakes/ppa -y && \
        apt-get update && \
        apt-get install -y python3.6 git && \
        curl https://bootstrap.pypa.io/get-pip.py | python3.6
RUN apt-get update -y && apt-get install -y python3-dev \
    python3-pip python3-setuptools python3-wheel
RUN apt-get install -y libpq-dev
RUN apt-get clean
RUN ln -s $(which python3.6) /usr/local/bin/python

COPY requirements.txt /requirements.txt

RUN pip install --upgrade pip && \
    pip install -r /requirements.txt

EXPOSE 8090

# Copy source files
COPY ./src/api /api

ENV PYTHONPATH /api


WORKDIR /api


CMD ["./wait-for-db.sh","python", "manage.py", "runserver", "0.0.0.0:8090"]