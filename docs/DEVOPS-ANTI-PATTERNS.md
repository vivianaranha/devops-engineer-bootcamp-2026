# DevOps Anti-Patterns

**Created by School of AI**

## Rebuilding per environment
Promote the same tested artifact instead.

## CI token with write-all
Grant only required permissions.

## Latest tags in production
Use immutable versions/digests.

## No rollback
Every production change needs a known recovery path.

## Liveness probe used as readiness
Restarting a temporarily unready app can amplify outages.

## Terraform apply without reviewed plan
Infrastructure changes deserve the same review discipline as code.

## Dashboards without SLOs
Charts are not reliability objectives.

## Platform team as a centralized ticket queue
Platforms should enable self-service and reduce cognitive load.

---

**Created by School of AI**
