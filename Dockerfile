FROM ubuntu:18.04
MAINTAINER DploY707 <starj1024@gmail.com>

# Install basic packages
RUN \
    apt-get update -y &&\
    apt-get install git zip curl unzip vim python3.8 python3-pip -y &&\
    apt-get update -y &&\
	update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.8 1

# Set Basic Env values
ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8


# Set projects directories
USER root
WORKDIR /root
# RUN \

# CMD ["python3","main.py"]
