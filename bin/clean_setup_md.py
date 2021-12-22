"""Clean up the setup.md files for better visual consistency.

The point of this script is to remove the frontmatter, which messes up the page
when the md is included. This also changes the depth of headings, as we want
the headings in the md files to be a lower lever than in the html template.
"""

import re
import yaml

def get_yaml_config():
    """Open the YAML config file for the website.

    Returns
    -------
    config: dict
        The configuration for the website.
    """

    with open("_config.yml", "r") as fp:
        config = yaml.load(fp, yaml.Loader)

    return config


def get_file_and_head(file, n_head=5):
    """Get the content of the file, and the head of it.

    Parameters
    ----------
    file: str
        The name of the file.
    n_head: int
        The number of lines to be included in the head.

    Returns
    -------
    content: str
        The content of the file.
    head: str
        The head of the file.
    """

    with open(file, "r") as fp:
        content = fp.read()
        fp.seek(0)
        head = [next(fp) for _ in range(n_head)]

    return content, head


website_config = get_yaml_config()

for lesson in website_config["lessons"]:

    file = f"_includes/rsg/{lesson['gh-name']}-lesson/setup.md"
    try:
        content, head = get_file_and_head(file)
    except StopIteration:
        print(f"{file} is empty, skipping clean up")
    content = content.splitlines()

    # Remove all the front matter (---) stuff, which messes up the page when
    # included in html

    if re.findall("---", "\n".join(head)):
        nfound = 0
        for i, line in enumerate(content):
            if line.startswith("---"):
                nfound += 1
            if nfound == 2:
                break
        content = content[i+1:]

    # Change the depth of headings

    for i, line in enumerate(content):
        if line.startswith("#"):
            line = line.rstrip("#")
            nhashes = line.count("#") + 2
            if nhashes > 5:
                nhashes = 5
            line = "#" * nhashes + line.lstrip("#")
            content[i] = line

    with open(file, "w") as fp:
        fp.write("\n".join(content))