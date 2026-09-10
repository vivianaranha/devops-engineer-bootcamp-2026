def golden_path_score(capabilities):
    expected={"repo_template","ci","security_scan","deployment","observability","rollback","runbook"}
    present=expected & set(capabilities)
    return {"score":round(len(present)/len(expected),4),"missing":sorted(expected-present)}
