def availability(success,total):
    return 0.0 if total<=0 else success/total

def error_budget(total_requests,slo_target):
    return max(0.0,total_requests*(1-slo_target))

def budget_remaining(total_requests,failed_requests,slo_target):
    budget=error_budget(total_requests,slo_target)
    return {"budget":budget,"used":failed_requests,"remaining":budget-failed_requests}
