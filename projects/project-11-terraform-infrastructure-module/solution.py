"""Project 11: Terraform Infrastructure Module."""
import json,sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]/"src"))
from devops_engineering.iac import validate_plan
def main():
    base=Path(__file__).resolve().parents[2]
    plan=json.loads((base/"data"/"iac_plan.json").read_text())
    print(validate_plan(plan))

if __name__=="__main__":
    main()
