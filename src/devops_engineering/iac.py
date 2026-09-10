REQUIRED_TAGS={"owner","environment","application"}

def validate_plan(plan):
    findings=[]
    for change in plan:
        if change.get("action")=="delete" and not change.get("approved"):
            findings.append({"resource":change.get("resource"),"issue":"unapproved_delete"})
        tags=set(change.get("tags",{}))
        missing=sorted(REQUIRED_TAGS-tags)
        if missing:
            findings.append({"resource":change.get("resource"),"issue":"missing_tags","tags":missing})
    return findings
