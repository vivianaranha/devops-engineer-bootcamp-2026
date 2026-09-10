"""Project 18: SRE Incident & SLO Pack."""
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]/"src"))
from devops_engineering.slo import budget_remaining
from devops_engineering.incident import incident_summary
def main():
    print(budget_remaining(100000,70,.999))
    print(incident_summary("INC-1","sev1",10,45))

if __name__=="__main__":
    main()
