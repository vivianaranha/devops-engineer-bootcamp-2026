def rollout_decision(error_rate,latency_ms,max_error_rate,max_latency_ms):
    checks={
        "error_rate":error_rate<=max_error_rate,
        "latency":latency_ms<=max_latency_ms,
    }
    return {"continue":all(checks.values()),"checks":checks}

def canary_split(total,percent):
    if not 0<=percent<=100: raise ValueError("percent must be 0..100")
    canary=round(total*percent/100)
    return {"canary":canary,"stable":total-canary}
