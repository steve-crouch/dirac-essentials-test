---
title: "Setting Up"
slug: dirac-version-control-setting-up-git
teaching: 5
exercises: 0
questions:
- "How do I get set up to use Git?"
- "How do I set up my account on GitHub?"
objectives:
- "Configure `git` the first time it is used on a computer"
- "Understand the meaning of the `--global` configuration flag"
- "Add an SSH key to a GitHub account"
keypoints:
- "Use `git config` with the `--global` option to configure a user name, email address, editor, and other preferences once per machine."
- "GitHub needs an SSH key to allow access"
---

> ## Prerequisites
>
> In this lesson we use Git from the Bash Shell.
> Some previous experience with the shell is expected,
> *but isn't mandatory*.
{: .prereq}

## Setting Up Git

**Linux and Mac** users should open a **terminal**, Windows users to should go to the Start Menu open GitBash from the Git group.

The first time we use Git on a new machine, we need to configure a few things.

~~~
$ cd
~~~
{: .language-bash}

Now we're going to set some global options, so when Git starts tracking changes to files it records who made them and how to contact them.

~~~
$ git config --global user.name "Firstname Surname"
$ git config --global user.email "fsurname@university.ac.uk"
~~~
{: .language-bash}

(Please use your own name and the email address you used to sign up to GitHub earlier!)

You can set your favourite text editor, following this table:

| Editor             | Configuration command                            |
|:-------------------|:-------------------------------------------------|
| nano               | `$ git config --global core.editor "nano -w"`    |
| Notepad++ (Win)    | `$ git config --global core.editor "'c:/program files (x86)/Notepad++/notepad++.exe' -multiInst -notabbar -nosession -noPlugin"`|


Git commands are written `git action`, where `action` is what we actually want it to do.
In this case, we're telling Git:

*   our **name** and **email address**,
*   what our favorite **text editor** is, and
*   that we want to use these settings **globally** (i.e., for every project),

The three commands above only need to be **run once**:
the flag `--global` tells Git to use the settings for every project on this machine.

You can check your settings at any time:

~~~
$ git config --list
~~~
{: .language-bash}

> ## Git Help and Manual
>
> If you forget a `git` command, you can access the list of commands by using `-h` and access the Git manual by using `--help` :
>
> ~~~
> $ git config -h
> $ git config --help
> ~~~
> {: .language-bash}
>
> While viewing the manual, remember the `:` is a prompt waiting for commands and you can press <kbd>Q</kbd> to exit the manual.
>
{: .callout}

{% include links.md %}
