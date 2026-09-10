# Tutorial 02.2 — Processes and Services

**Created by School of AI**

**Module:** Linux for DevOps Engineers

## Objective

Engineer **processes and services** as part of a secure, repeatable delivery system.

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

Linux troubleshooting should start with observable facts: process state, ports, logs, CPU, memory, disk and network—not random restarts.

## Hands-on checkpoint

Create one implementation/design artifact, one automated gate, one failure/rollback scenario and one operational metric.

---

**Created by School of AI**
