#!/bin/bash

CURRENT_DATE=$(date +"%Y%m%d_%H%M")

build_container () {
	CONTAINER_NAME=record-stream
	TAG=0.1
	echo "Current date set to $CURRENT_DATE"
	sudo docker build -t "$CONTAINER_NAME:$TAG" .
}

cleanup_images () {
	sudo docker images -a | grep "record"| awk '{print $3}'| xargs sudo docker rmi -f
}
