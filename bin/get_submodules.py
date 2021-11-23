""" Parse the curriculum collection and add sunmodules """

import os
from yaml import load
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

os.system('pwd')
os.system('ls')
os.system("rm -rf submodules")

os.system("mkdir -p submodules")

with open('_data/lessons.yml') as config:
    data = load(config, Loader=Loader)
    for lesson_info in data['lessons']:
        if lesson_info.get('type', None) == 'episode':
            # Create the command to pull the subdirectory from GitHub
            lesson_name = lesson_info.get('gh-name', None)
            gh_branch = lesson_info.get('branch', 'gh-pages')
            command = f"git submodule add --force -b {gh_branch} https://github.com/Southampton-RSG-Training/{lesson_name}.git submodules/{lesson_name}"
            os.system(command)
            os.system("git submodule update --remote --merge")
            # move required files from the subdirectories to _includes/rsg/{lesson_name}/...

            # make directory
            dest = f"_includes/rsg/{lesson_name}"
            os.system(f"mkdir -p {dest}")
            for file in ["setup.md", "_includes/rsg/schedule.html"]:
                os.system(f"cp submodules/{lesson_name}/{file} {dest}/{file.split('/')[-1]}")

            for directory in ["_episodes", "_episodes_rmd"]:
                dest = f"collections/{directory}/{lesson_name}"
                os.system(f"mkdir -p {dest}")
                os.system(f"cp -r submodules/{lesson_name}/{directory}/ {dest}/")
            for file in ["reference.md"]:
                dest = f"collections/_episodes/{lesson_name}"
                os.system(f"mkdir -p {dest}")
                os.system(f"cp submodules/{lesson_name}/{file} {dest}/{file.split('/')[-1]}")
            # Copy the figures from submodule into fig
            os.system(f"cp -r submodules/{lesson_name}/fig/ fig/")
            # If the lesson has assoiated slides
            try:
                os.system(f"cp -r submodules/{lesson_name}/slides ./")
            except:
                print(f"{lesson_name} has no slides")

