# Operations Runbook

## Verify Triton Deployment

Check pods:

```bash
kubectl get pods
```

Expected:

```text
triton-server Running
```

Check logs:

```bash
kubectl logs deployment/triton-server
```

---

## Verify vLLM Deployment

Check deployment:

```bash
kubectl get deployment vllm
```

Check logs:

```bash
kubectl logs deployment/vllm
```

---

## Verify GPU Allocation

Execute:

```bash
kubectl exec -it <pod> -- nvidia-smi
```

Expected:

GPU visible inside container.

---

## Verify Device Plugin

```bash
kubectl get pods -n kube-system
```

Expected:

```text
nvidia-device-plugin Running
```

---

## Verify Metrics

```bash
curl prometheus:9090/targets
```

Expected:

Targets UP.

---

## Verify Dashboard

Open Grafana dashboard.

Confirm:

- GPU Utilization
- GPU Memory
- Triton Status
- vLLM Status

are visible.

---

## Verify Helm Release

```bash
helm list
```

Expected:

```text
gpu-inference-platform
```