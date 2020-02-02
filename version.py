import git, re
    
def version():
    repo = git.Repo("./")

    descr = repo.git.describe('--abbrev=0', '--tags', '--always')

    #version().git.describe('--abbrev=0', '--tags', '--always')

    m = re.search("v([0-9]*)\\.([0-9]*)\\.([0-9]*)", descr)

    if not m:
        return "v0.0.0"

    return m.group(0)
