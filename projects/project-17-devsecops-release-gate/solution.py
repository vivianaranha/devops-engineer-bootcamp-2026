"""Project 17: DevSecOps Release Gate."""
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]/"src"))
from devops_engineering.security import pipeline_security_review
def main():
    cfg={"token_permissions":"write-all","secrets_in_repo":False,"dependency_scan":True,"artifact_checksum":False}
    print(pipeline_security_review(cfg))

if __name__=="__main__":
    main()
