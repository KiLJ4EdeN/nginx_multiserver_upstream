FROM python:3.6

MAINTAINER KiLJ4EdeN

# os level reqs
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y --fix-missing \
    build-essential \
    cmake \
    gfortran \
    pkg-config \
    python3-dev \
    software-properties-common \
    && apt-get clean && rm -rf /tmp/* /var/tmp/*

COPY . /app
WORKDIR /app

# python reqs
RUN pip3 install --upgrade pip
RUN pip3 install setuptools wheel
RUN pip3 install flask


CMD ["python", "main.py"]