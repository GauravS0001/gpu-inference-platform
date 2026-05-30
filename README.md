# GPU Inference Platform

Production-style Kubernetes GPU inference platform demonstrating:

- Triton Inference Server
- vLLM Deployments
- GPU Resource Scheduling
- Kubernetes Deployments
- AI Inference Workloads
- Production Inference Operations

## Components

### Triton

Used for model serving and multi-model inference.

### vLLM

Used for LLM serving with optimized GPU memory usage.

### Kubernetes

Schedules GPU workloads using:

```yaml
resources:
  limits:
    nvidia.com/gpu: 1
```

## Deployment

Deploy Triton:

```bash
kubectl apply -f triton/
```

Deploy vLLM:

```bash
kubectl apply -f vllm/
```

Verify:

```bash
kubectl get pods
```


## Helm Commands

helm lint ./helm/gpu-inference-platform

helm template gpu-inference-platform \
./helm/gpu-inference-platform

helm install gpu-inference-platform \
./helm/gpu-inference-platform

helm upgrade gpu-inference-platform \
./helm/gpu-inference-platform