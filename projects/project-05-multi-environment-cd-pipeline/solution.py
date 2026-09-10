"""Project 05: Multi-Environment CD Pipeline."""
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]/"src"))
from devops_engineering.deployment import rollout_decision,canary_split
def main():
    print(canary_split(100,10))
    print(rollout_decision(.004,180,.01,250))
    print(rollout_decision(.02,300,.01,250))

if __name__=="__main__":
    main()
