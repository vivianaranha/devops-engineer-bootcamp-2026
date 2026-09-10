"""Project 19: Internal Developer Platform Blueprint."""
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]/"src"))
from devops_engineering.platform import golden_path_score
def main():
    print(golden_path_score(["repo_template","ci","security_scan","deployment","observability"]))

if __name__=="__main__":
    main()
