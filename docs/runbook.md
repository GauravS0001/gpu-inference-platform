# Runbook

## Pod Pending

Check:

kubectl describe pod

Possible Causes:

- No GPUs available
- Device Plugin missing
- GPU node unavailable

---

## GPU Not Visible

Check:

kubectl exec -it pod-name -- nvidia-smi

---

## Image Pull Failure

Check:

kubectl describe pod

---

## CrashLoopBackOff

Check:

kubectl logs pod-name

---

## Service Unreachable

Check:

kubectl get svc -n inference