# Deployment Guide

Build image

docker build -t inference-api:v1 .

Load image

kind load docker-image inference-api:v1

Deploy namespace

kubectl apply -f kubernetes/namespace.yaml

Deploy application

kubectl apply -f kubernetes/deployment.yaml

Deploy service

kubectl apply -f kubernetes/service.yaml

Verify

kubectl get pods -n inference