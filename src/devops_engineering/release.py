import hashlib
from pathlib import Path

def sha256(path):
    h=hashlib.sha256()
    with Path(path).open("rb") as f:
        for chunk in iter(lambda:f.read(65536),b""):
            h.update(chunk)
    return h.hexdigest()

def release_allowed(checks):
    failed=[name for name,ok in checks.items() if not ok]
    return {"allowed":not failed,"failed":failed}
