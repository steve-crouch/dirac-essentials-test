""" Parse the curriculum collection and add sunmodules """

import os
from yaml import load
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

os.system('pwd')

os.system("mkdir -p submodules")

with open('_data/lessons.yml') as config:
    data = load(config, Loader=Loader)
    for episode_info in data['lessons']:
        if episode_info.get('type', None) == 'episode':
            # Create the command to pull the subdirectory from GitHub
            episode_name = episode_info.get('gh-name', None)
            gh_branch = episode_info.get('branch', 'gh-pages')
            command = f"git submodule add --force -b {gh_branch} https://github.com/Southampton-RSG-Training/{episode_name}.git submodules/{episode_name}"
            os.system(command)
            os.system("git submodule update --remote --merge")
            # move required files from the subdirectories to _includes/rsg/{episode_name}/...
            # make directory
            dest = f"_includes/rsg/{episode_name}"
            os.system(f"mkdir -p {dest}")
            for directory in ["_episodes", "_episodes_rmd", "fig"]:
                os.system(f"cp -r submodules/{episode_name}/{directory} {dest}/{directory}")
            for file in ["index.md", "setup.md", "_includes/rsg/schedule.html"]:
                os.system(f"cp submodules/{episode_name}/{file} {dest}/{file.split('/')[-1]}")

            # Copy the figures from submodule into fig
            os.system(f"cp -r submodules/{episode_name}/fig/ fig/")
            # If the lesson has assoiated slides
            try:
                os.system(f"cp -r submodules/{episode_name}/slides ./")
            except:
                print(f"{episode_name} has no slides")

