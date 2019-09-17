
The publisher publishes the face image read from the camera to the jetsonimage topic. The subscriber subcribes to jetsonimage topic to receive the face image read from the camera and then forwards it to the remote by publishing to the cloudfaceimage topic. 

Topic on the jetson side - jetsonimage
Topic on the IBM VSI side - cloudfaceimage

The subscriber subcribes to cloudfaceimage to receive the face image from the jetson and uploads to object storage. 

QoS used was the default of 0. In this case, we didn't need a guarantee of every message being delivered, also we had a stable connection between the sender and receiver.

Steps performed:
Jetson

    create network bridge

    sudo docker network create --driver bridge hw03

    create mosquitto container

    sudo docker run --name mosquitto --network hw03 -p 1883:1883 mosquitto

    create face detetctor container

    sudo docker run --name detector --network hw03 --device=/dev/video1:/dev/video1 -ti detector /bin/bash

    once inside bash run - python facedetector.py

    create forwarder container to forward the messages to VSI

    sudo docker run --name forwarder --network hw03 -ti faceforwarder sh

    once inside shell client run - python3 forwarder.py

IBM VSI

    create network bridge

    docker network create --driver bridge hw03

    create mosquitto container

    docker run --name mosquitto --network hw03 -p 1883:1883 mosquitto

    create uploader container to upload the faces to object storage

    docker run --name uploader --network hw03 -ti uploader sh

    once inside shell client run - python upload.py
