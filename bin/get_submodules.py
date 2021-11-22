""" Parse the curriculum collection and add sunmodules """

import os
from yaml import load
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

os.system('pwd')
os.system('ls')

os.system("mkdir -p submodules")

with open('_config.yml') as config:
    data = load(config, Loader=Loader)
    for episode_info in data['collections']:
        if data['collections'][episode_info].get('type', None) == 'episode':
            # Create the command to pull the subdirectory from GitHub
            episode_name = data['collections'][episode_info].get('label', None)
            gh_branch = data['collections'][episode_info].get('branch', 'gh-pages')
            command = f"git submodule add -b {gh_branch} https://github.com/Southampton-RSG-Training/{episode_name}.git submodules/{episode_name}"
            os.system(command)
            # move required files from the subdirectories to _includes/rsg/{episode_name}/...
            # make directory
            dest = f"_includes/rsg/{episode_name}"
            os.system(f"mkdir -p {dest}")
            for directory in ["_episodes", "_episodes_rmd", "fig"]:
                os.system(f"cp -r submodules/{episode_name}/{directory} {dest}/{directory}")
            for file in ["index.md", "setup.md"]:
                os.system(f"cp submodules/{episode_name}/{file} {dest}/{file}")

