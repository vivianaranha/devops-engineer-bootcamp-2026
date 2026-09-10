"""Project 10: Kubernetes Production Hardening."""
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]/"src"))
from devops_engineering.k8s import resource_findings,probe_review
def main():
    print(resource_findings("250m","500m","256Mi","512Mi"))
    print(probe_review("/ready","/health"))

if __name__=="__main__":
    main()
