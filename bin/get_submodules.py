""" Parse the curriculum collection and add submodules """

import os
from yaml import load
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader

os.system("rm -rf submodules")
os.system("rm -rf collections")
os.system("rm -rf slides")

with open('_config.yml') as config:
    data = load(config, Loader=Loader)

print(f"Getting submodules specified in {data['lessons']}")
os.system("mkdir -p submodules")

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

# Now need to do the same for slides, but have to do it afterwards because we
# need a specific version of reveal.js, so we need to avoid the git submodule
# update

os.system("git submodule add --force https://github.com/hakimel/reveal.js.git submodules/reveal.js")
os.system("cd submodules/reveal.js && git checkout 8a54118f43")

for lesson_info in data['lessons']:
    if lesson_info.get('type', None) in ["episode", "episode_r"]:
        lesson_name = lesson_info.get('gh-name', None)
        os.system(f"mkdir -p slides/{lesson_name}-lesson/")
        os.system(f"cp -r submodules/{lesson_name}/slides/* slides/{lesson_name}-lesson/")
        # The lesson reveal.js submodule folder is empty, so delete and copy
        # reveal.js into the folder instead
        os.system(f"rm -r slides/{lesson_name}-lesson/reveal.js")
        os.system(f"cp -r submodules/reveal.js slides/{lesson_name}-lesson/")
