"""Project 03: Build Artifact Pipeline."""
import tempfile,sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]/"src"))
from devops_engineering.release import sha256
def main():
    with tempfile.TemporaryDirectory() as d:
        p=Path(d)/"artifact.txt"; p.write_text("build-v1")
        print({"artifact":p.name,"sha256":sha256(p)})

if __name__=="__main__":
    main()
