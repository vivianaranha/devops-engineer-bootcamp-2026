def parse(version):
    parts=version.lstrip("v").split(".")
    if len(parts)!=3: raise ValueError("expected MAJOR.MINOR.PATCH")
    return tuple(int(x) for x in parts)
def bump(version,kind):
    major,minor,patch=parse(version)
    if kind=="major": return f"{major+1}.0.0"
    if kind=="minor": return f"{major}.{minor+1}.0"
    if kind=="patch": return f"{major}.{minor}.{patch+1}"
    raise ValueError("kind must be major/minor/patch")
