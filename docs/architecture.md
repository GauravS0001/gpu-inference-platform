# Architecture

Kubernetes

├── Inference API

├── NVIDIA Device Plugin

├── GPU Enabled Worker Node

└── Prometheus

Inference workloads request GPU resources through:

nvidia.com/gpu: 1

The NVIDIA Device Plugin advertises GPU resources to Kubernetes and enables scheduling of GPU workloads.