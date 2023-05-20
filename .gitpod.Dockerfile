FROm iron/python:2.7

RUN sudo apt-get update && \
    sudo apt-get install -y git && \
    sudo apt-get clean && \
    sudo rm -rf /var/cache/apt/* /var/lib/apt/lists/* /tmp/*
