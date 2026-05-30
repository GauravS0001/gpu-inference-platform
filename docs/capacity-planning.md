# Capacity Planning Guide

## Objective

Determine when additional GPU resources are required.

---

## Metrics To Monitor

GPU Utilization

Target:

60-80%

Investigate when:

>90%

---

GPU Memory Usage

Target:

Below 80%

Investigate when:

>90%

---

Inference Latency

Monitor:

- P95 Latency
- P99 Latency

Increasing latency may indicate:

- GPU saturation
- insufficient replicas
- oversized models

---

## Scaling Options

### Horizontal Scaling

Increase replicas:

```yaml
replicas: 3
```

---

### Vertical Scaling

Move workloads to:

- Larger GPUs
- Additional GPUs

Example:

A100 → Multiple A100

---

### Autoscaling

Use HPA:

```bash
kubectl get hpa
```

Verify scaling activity.

---

## Capacity Review Checklist

Weekly:

- GPU utilization
- GPU memory utilization
- pod restarts
- inference latency

Monthly:

- forecast GPU demand
- review cluster growth
- evaluate model resource usage