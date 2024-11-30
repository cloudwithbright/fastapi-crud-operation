#!/bin/bash

# Azure
az acr login --name 

docker buildx build --platform linux/arm64/v8,linux/amd64 \
  -t gtuccr.azurecr.io/backend \
  --push \
  .

# AWS
docker buildx build --platform linux/arm64/v8,linux/amd64 \
  -t 031767307411.dkr.ecr.us-east-2.amazonaws.com/items:latest \
  --push .