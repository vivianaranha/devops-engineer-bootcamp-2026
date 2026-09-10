def resource_findings(cpu_request,cpu_limit,memory_request,memory_limit):
    findings=[]
    if not cpu_request: findings.append("missing_cpu_request")
    if not memory_request: findings.append("missing_memory_request")
    if cpu_limit and cpu_request and cpu_limit<cpu_request: findings.append("cpu_limit_below_request")
    if memory_limit and memory_request and memory_limit<memory_request: findings.append("memory_limit_below_request")
    return findings

def probe_review(readiness,liveness):
    return {"ready":bool(readiness),"live":bool(liveness),"production_ready":bool(readiness and liveness)}
