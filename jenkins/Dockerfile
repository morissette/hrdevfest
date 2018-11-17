FROM jenkins/jenkins:latest
USER root
RUN apt-get update && apt-get install -y \
    python-pip \
    mongodb \
    vim \
    libyaml-dev \
    software-properties-common
RUN echo "deb http://ppa.launchpad.net/ansible/ansible/ubuntu trusty main" >> /etc/apt/sources.list
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 93C4A3FD7BB9C367
RUN apt-get update && apt-get install -y ansible
RUN mkdir /root/.ssh
RUN chmod 700 /root/.ssh
COPY keys/dev_rsa /root/.ssh/id_rsa
RUN chmod 600 /root/.ssh/id_rsa
