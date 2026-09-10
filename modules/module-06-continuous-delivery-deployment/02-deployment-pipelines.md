# Tutorial 06.2 — Deployment Pipelines

**Created by School of AI**

**Module:** Continuous Delivery & Deployment

## Objective

Engineer **deployment pipelines** as part of a secure, repeatable delivery system.

## 1. Define the delivery outcome

Record:
- source/change,
- validation,
- artifact,
- environment,
- promotion decision,
- rollback path,
- operator owner.

## 2. Automate the repeatable work

Good candidates:
- tests,
- linting,
- builds,
- artifact checksums,
- image builds,
- policy checks,
- deployment,
- health verification.

## 3. Make failure safe

Define:
- timeout,
- retry,
- rollback,
- approval,
- failure notification,
- recovery owner.

## 4. Preserve traceability

Be able to connect:
**commit → workflow run → artifact → image/digest → deployment → production version**.

## 5. Measure the system

Consider:
- deployment frequency,
- lead time,
- change failure rate,
- recovery time,
- availability/error budget,
- pipeline duration.

Continuous delivery means every change can be released safely; continuous deployment additionally automates production release.

## Hands-on checkpoint

Create one implementation/design artifact, one automated gate, one failure/rollback scenario and one operational metric.

---

**Created by School of AI**
