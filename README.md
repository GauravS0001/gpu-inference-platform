# GPU Inference Platform

A Kubernetes-based GPU inference platform demonstrating GPU workload scheduling, containerized inference services, monitoring integration, and operational runbooks.

## Features

- GPU-enabled Kubernetes deployment
- NVIDIA Device Plugin integration
- GPU resource requests
- Containerized inference API
- Prometheus monitoring
- Operational documentation

## Deployment

kubectl apply -f kubernetes/

## GPU Resource Example

resources:
  limits:
    nvidia.com/gpu: 1