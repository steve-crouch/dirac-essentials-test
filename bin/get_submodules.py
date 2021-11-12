""" Parse the curriculum collection and add sunmodules """

import os
from yaml import load
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

os.system('pwd')
os.system('ls')

with open('_config.yml') as config:
    data = load(config, Loader=Loader)
    for episode_info in data['curriculum']:
        episode_name = data['curriculum'][episode_info].get('name', None)
        gh_branch = data['curriculum'][episode_info].get('branch', 'gh-pages')
        command = f"git submodule add -b {gh_branch} https://github.com/Southampton-RSG-Training/{episode_name}.git _episodes/{episode_name}"
        os.system(command)

