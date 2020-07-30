#!/bin/bash


echo "Creating the volume..."

kubectl apply -f ./kubernetes/persistent-volume.yml
kubectl apply -f ./kubernetes/persistent-volume-claim.yml


echo "Creating the database credentials..."

kubectl apply -f ./kubernetes/secret.yml


echo "Creating the postgres deployment and service..."

kubectl create -f ./kubernetes/database-deployment.yml
kubectl create -f ./kubernetes/database-service.yml



echo "Creating the server deployment and service..."

kubectl create -f ./kubernetes/server-deployment.yml
kubectl create -f ./kubernetes/server-service.yml


echo "Adding the ingress..."

#minikube addons enable ingress
#kubectl apply -f ./kubernetes/minikube-ingress.yml


echo "Creating the client deployment and service..."

kubectl create -f ./kubernetes/client-deployment.yml
kubectl create -f ./kubernetes/client-service.yml