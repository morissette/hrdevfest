#!/bin/bash
# set docker images to use minikube
eval $(minikube docker-env)

# make sure right kubectl is set
minikube update-context

# build images
find . -type f -name Dockerfile | while read file;
do 
    service=$(dirname $file | cut -d '/' -f2)
    docker build -t $service $service
done

# push changes
if [[ $(kubectl get pods 2>&1) == 'No resources found.' ]]; then
    $(kubectl create -f config/k8s_deployments.yml)
else
    $(kubectl replace -f config/k8s_deployments.yml)
fi
