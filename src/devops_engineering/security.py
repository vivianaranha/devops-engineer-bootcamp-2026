def pipeline_security_review(config):
    findings=[]
    if config.get("token_permissions")=="write-all": findings.append("excessive_ci_token_permissions")
    if config.get("secrets_in_repo"): findings.append("secrets_in_repository")
    if not config.get("dependency_scan"): findings.append("missing_dependency_scan")
    if not config.get("artifact_checksum"): findings.append("missing_artifact_checksum")
    return findings
