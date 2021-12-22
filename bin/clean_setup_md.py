"""Clean up the setup.md files for better visual consistency.

"""

import re
import yaml
from enum import Enum

class LessonType(Enum):
    """Enum for the different types of lessons.
    """
    markdown = "episode"
    r_markdown = "episode_r"


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

    print(file)

    with open(file, "r") as fp:
        content = fp.read()
        fp.seek(0)
        try:
            head = [next(fp) for _ in range(n_head)]
        except StopIteration:
            head = []

    return content, head


website_config = get_yaml_config()


for lesson in website_config["lessons"]:
    lesson_type = LessonType(lesson.get("type", None))

    file = f"_includes/rsg/{lesson['gh-name']}-lesson/setup.md"
    content, head = get_file_and_head(file)

    content = content.splitlines()

    # Remove the front matter --- stuff

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