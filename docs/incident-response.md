# Incident Response Guide

## Incident: Triton Failure

Symptoms

- inference requests failing
- service unavailable

Checks

```bash
kubectl logs deployment/triton-server
```

Resolution

- validate model repository
- restart deployment

---

## Incident: vLLM Failure

Symptoms

- API unavailable
- model load failures

Checks

```bash
kubectl logs deployment/vllm
```

Resolution

- validate model configuration
- verify GPU allocation

---

## Incident: GPU Saturation

Symptoms

- increased latency
- timeout errors

Checks

```bash
nvidia-smi
```

Review:

- utilization
- memory usage

Resolution

- scale replicas
- reduce workload

---

## Incident: Device Plugin Failure

Symptoms

Pods remain Pending.

Checks

```bash
kubectl get pods -n kube-system
```

Resolution

Restart NVIDIA Device Plugin.

---

## Incident: Prometheus Not Scraping

Symptoms

Dashboard empty.

Checks

```bash
curl prometheus:9090/targets
```

Resolution

Validate:

- ServiceMonitor
- scrape targets
- service labels