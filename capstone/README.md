# Production DevOps Platform — Capstone

**Created by School of AI**

## Scenario

Build **Northstar Delivery Platform**, an enterprise software-delivery system for a web/API application.

## Required lifecycle

**Git Commit**
→ **Pull Request**
→ **CI Tests**
→ **Security Gates**
→ **Immutable Artifact/Image**
→ **Registry**
→ **Terraform Plan**
→ **Environment Promotion**
→ **Kubernetes Deployment**
→ **Health Verification**
→ **Prometheus/Grafana**
→ **Central Logs**
→ **SLO/Error Budget**
→ **Incident Response / Rollback**

## Required deliverables

1. value-stream map
2. Git workflow
3. build/artifact manifest
4. GitHub Actions CI
5. CD environment model
6. Dockerfile
7. Docker Compose local design
8. container supply-chain plan
9. Kubernetes manifests
10. probe/resource/autoscaling design
11. Terraform module/workflow
12. cloud deployment mapping
13. configuration/secrets plan
14. observability architecture
15. Prometheus/Grafana dashboard design
16. centralized logging/correlation
17. DevSecOps release gate
18. SLO/error budget
19. incident/postmortem process
20. internal developer golden path
21. rollback/runbook
22. executive delivery metrics

## Demo scenarios

- failing test blocks merge/release
- CI token permissions are least-privileged
- artifact checksum identifies exact build
- bad canary health stops rollout
- Kubernetes readiness removes unhealthy workload from traffic
- Terraform plan with unapproved delete is rejected
- secret is not stored in repository
- latency/error alert maps to SLO
- release pauses when error budget policy requires it
- rollback returns to previous known-good version

---

**Created by School of AI**
