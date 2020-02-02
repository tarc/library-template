import git, re
    
def version():
    repo = git.Repo(search_parent_directories=True)

    descr = repo.git.describe('--abbrev=0', '--tags', '--always')

    m = re.search("v(([0-9]*)\\.([0-9]*)\\.([0-9]*))", descr)

    if not m:
        return ("0.0.0", "0", "0", "0")

    return (m.group(1), m.group(2), m.group(3), m.group(4))

def write_version_header(file_name, header_guard, namespace, major, minor, patch):
    contents=f"""
#ifndef {header_guard}
#define {header_guard}

namespace {namespace} {{

  constexpr int major_version_number = {major};

  constexpr int minor_version_number = {minor};

  constexpr int patch_version_number = {patch};

}} // namespace {namespace}

#endif // {header_guard}
"""

    with open(file_name, "w") as version_hpp:
        version_hpp.write(contents)
