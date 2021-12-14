""" Parse the curriculum collection and add submodules """

import os
from yaml import load
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

os.system("rm -rf submodules")
os.system("mkdir -p submodules")

with open('_config.yml') as config:
    data = load(config, Loader=Loader)
    print(f"Getting submodules specified in {data['lessons']}")
    for lesson_info in data['lessons']:
        if lesson_info.get('type', None) in ["episode", "episode_r"]:
            if lesson_info.get('type', None) == 'episode':
                directory = "_episodes"
            elif lesson_info.get('type', None) == 'episode_r':
                directory = "_episodes_rmd"

            # Create the command to pull the subdirectory from GitHub
            lesson_name = lesson_info.get('gh-name', None)
            gh_branch = lesson_info.get('branch', 'gh-pages')
            print(f"Getting lesson with parameters:\n gh-name: {lesson_name} \n branch: {gh_branch} \n type: {directory}")

            command = f"git submodule add --force -b {gh_branch} https://github.com/Southampton-RSG-Training/{lesson_name}.git submodules/{lesson_name}"
            os.system(command)
            os.system("git submodule update --remote --merge")
            # move required files from the subdirectories to _includes/rsg/{lesson_name}/...

            # lesson destinations need to be appended with -lesson to avoid gh-pages naming conflicts
            # make directory
            dest = f"_includes/rsg/{lesson_name}-lesson"
            os.system(f"mkdir -p {dest}")
            for file in ["setup.md", "_includes/rsg/schedule.html"]:
                os.system(f"cp submodules/{lesson_name}/{file} {dest}/{file.split('/')[-1]}")

            dest = f"collections/{directory}/{lesson_name}-lesson"
            os.system(f"mkdir -p {dest}")
            print(f"cp -r submodules/{lesson_name}/{directory}/. {dest}/")
            os.system(f"cp -r submodules/{lesson_name}/{directory}/. {dest}/")
            for file in ["reference.md", "setup.R", "renv.lock"]:
                try:
                    dest = f"collections/{directory}/{lesson_name}-lesson"
                    os.system(f"mkdir -p {dest}")
                    os.system(f"cp submodules/{lesson_name}/{file} {dest}/{file.split('/')[-1]}")
                except:
                    print(f"collections/{directory}/{lesson_name}-lesson/{file}" + ": Cannot be found/moved")

            os.system(f"cp -r submodules/{lesson_name}/fig/. fig/")
            # If the lesson has associated slides
            try:
                os.system(f"cp -r submodules/{lesson_name}/slides ./")
            except:
                print(f"{lesson_name} has no slides")

