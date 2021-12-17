## RSG Training Workshop Template

##### To use this repository please use the template functionality. When you use the template give the new repository a descriptive name as it will become the url base that is provided to learners.

### Setting up a workshop

To configure a workshop please follow the steps below.

1) Create a copy of this workshop using the GitHub (GH) templating function. Note the name of your new workshop will be the website URL so be descriptive and accurate.
2) Using either the GH online code editor or pulling a local version edit the _config.yml file. This is the only file that needs to be modified.
3) The fields to change are as follows:
   1) carpentry: default 'rsg', uses the rsg templating build process.
   2) title, venue, address, country, lat/long: Updates the details for location.
   3) humandate, humantime, startdate, enddate: human and machine-readable dates and times to start the lesson.
   4) instructor, instructor-email: YAML lists of instructor names and associated email addresses.
   5) helper: Names of helpers.
   6) **lessons: list of lessons to include in the workshop, each lesson must have.**
      1) title: Name to give to the lesson.
      2) gh-name*: Name of a lesson repository in the <https://github.com/Southampton-RSG-Training>  GH organisation e.g. 'git-novice'.
      3) type: choose from 'episode' for standard, 'episode_r' for rmarkdown 
      4) branch: Default: 'gh-pages', to customise, one can specify another branch - more details below.
      5) date: Date lesson is to be taught, many date formats accepted (TODO: Ed list the accepted formats). For multi day lessons, dates can be given as a list e.g. see python-novice example.
      6) time: Time to start lesson, many time formats accepted (TODO: Ed list the accepted formats). For multi day lessons times can be given as a list.
4) **Commit (and push) changes to the 'main'** branch the site is then built and published on the 'gh-pages' branch. The site build is handled by GH Actions, more details in development below.
5) **Commit 

*Available lesson names are:

- shell-novice <https://github.com/Southampton-RSG-Training/shell-novice>
- git-novice <https://github.com/Southampton-RSG-Training/git-novice>
- python-novice <https://github.com/Southampton-RSG-Training/python-novice>
- spreadsheets <https://github.com/Southampton-RSG-Training/spreadsheets>
- openrefine-data-cleaning <https://github.com/Southampton-RSG-Training/openrefine-data-cleaning>
- r-novice <https://github.com/Southampton-RSG-Training/r-novice>
- project-novice <https://github.com/Southampton-RSG-Training/project-novice>

### Customising Lessons

To customise a lessons content the lesson branch can be changed in the lessons' collection to reflect an alternative 
branch of a lesson repository. You can then stage (add) and commit '_config.yml', save the push to remote until after 
the episode branch has been created/edited as the push will then grab the changes.

To make changes to the lessons clone the lesson repository and then checkout (or create) branch for the modified lesson 
you want. **Note the gh-pages branch is the canonical branch and shouldn't be edited for lesson customisation**. To 
modify lesson content edit the markdown in _episodes (or _episodes_rmd for courses written in R markdown). Commit and 
push your changes to the lesson repository on the (new) branch used for the custom material. The workshop repository
(templated from workshop-template) then needs to be updated use the following commit command to create an empty rebuild 
push if you have not got a staged commit of '_config.yml' if you do then you only need to push to remote.
  
    $ git commit --allow-empty -m "rebuild lesson to (re)add lesson submodules"
    $ git push origin main

If you think the changes are a universal improvement to the base gh-pages branch please open a pull request for review.

### Development Guide and Build logic

To develop this template requires an understanding of: **jekyll/liquid** used in the deployment of static GitHub pages 
sites; **GitHub Actions** and **python** used to parse the '_config.yml', clone submodules, and move/generate files; 
**markdown** and or **Rmarkdown** used to write the lesson material; **GitHub/git (especially branches)** we use 
branches to manage lesson version, and to separate configuration from deployment.


The gh-pages branch of each lesson are kept in a build ready state. Development for these lessons is detailed in each 
lesson repository. 
The config file is used by the jekyll build and also parsed to control the GitHub Actions. Firstly, the _config.yml is 
parsed by 'get_submodules.py' and 'get_schedules.py'. 
'get_submodules.py' gets each of the lesson repositories and clones them as a submodule, the episode markdown files are 
moved into collections/_episodes(_rmd)/gh-name-lesson/ then the GH Pages process (Jekyll/Liquid) is instructed to build 
them via the config.yml as the episodes are specified in the collections as output with the slug acting as a permalink.
'get_submodules.py' also moves the schedule and setup into _includes/rsg/gh-name-lesson/, from there the GH Pages 
process (Jekyll/Liquid) includes the setup and schedule on the workshop's homepage.
Finally, 'get_schedules.py' runs after 'get_submodules.py' but before the GH Pages process (Jekyll/Liquid) it uses the 
time and date specified in config to update the schedule.


