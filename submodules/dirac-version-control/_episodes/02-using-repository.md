---
title: "Using a Repository"
slug: dirac-version-control-using-repository
teaching: 10
exercises: 0
questions:
- "How do I create a version control repository?"
- "Where does Git store information?"
objectives:
- "Create a repository from a template."
- "Clone and use a Git repository."
- "Describe the purpose of the `.git` directory."
keypoints:
- "`git clone` creates a local copy of a repository from a URL."
- "Git stores all of its repository data in the `.git` directory."
---

# Creating a Repository

A **repository** is a directory that is under **version control** - it can track changes to files within it. Git also makes it easy to sync up a **local repository** on your computer with a **remote repository** on the internet (or intranet!). 

## Using a Template

We're going to work with some pre-existing template code, that's already stored in a repository. The first thing we need to do is create our own copy of that template, which we can do on [GitHub](https://github.com). First, visit [GitHub](https://github.com), and make sure you've signed in to your account.

Once you're signed in, [go to our template repository](https://github.com/Southampton-RSG-Training/dirac-version-control-template) and select **Use this template**:

![Use Template]({{ site.url }}{{ site.baseurl }}/fig/02-using-repository/template-copy.png)

We should get prompted to give details for what we'd like our copy of the template to be called. As this demo code is for analysing climate data, we'll name our copy of it `climate-analysis`. We also want it to be public, so anyone can see and copy our code:

![Repository Details]({{ site.url }}{{ site.baseurl }}/fig/02-using-repository/template-details.png)

> ## Public or Private?
> GitHub will allow you to create private repositories, so only people you specify can access the code, but it's always best to keep your code public - especially if you're going to use it in a paper! Code that generates or analyses data is a fundamental part of your method, and if you don't include your full method in papers your work can't be reproduced, and reproducibility is key to the scientific process. **Always** keep your repositories public unless you've got a strong reason, like embargoes imposed by industrial partners.
>
> A major advantage of this is if you leave academia, or you switch institution and forget to update the email on your GitHub account before you lose your old one, your work won't be lost forever!
{: .callout}

After a brief wait, GitHub will have created a **remote repository** - a copy of the files and their history stored on GitHub's servers. We want to copy that to our local machine, which we do using `git clone`. Click on the **code** button, and you should have a choice of ways to copy the code. Select **SSH**, then click the copy button to copy the repository's URL:

![Copy Repository URL]({{ site.url }}{{ site.baseurl }}/fig/02-using-repository/repository-url.png)

~~~
$ git clone git@github.com:smangham/climate-analysis.git
~~~
{: .language-bash}

~~~
Cloning into 'climate-analysis'...
remote: Enumerating objects: 4, done.
remote: Counting objects: 100% (4/4), done.
remote: Compressing objects: 100% (4/4), done.
remote: Total 4 (delta 0), reused 3 (delta 0), pack-reused 0
Receiving objects: 100% (4/4), done.
~~~
{: .output}

Now, if we use `ls` to list the contents of the directory, we should see we have a new directory, called `climate-analysis`, that's a **local repository** containing the code from our **remote repository**. This is linked up automatically - making it easy for us to download updates to the remote repository, or to send our changes back up to it.

> ## Creating Repositories Locally
> 
> You don't have to create your repositories on GitHub first!
> If you want, you can create a repository locally by entering any directory and using `git init`. From there, you can use the other commands we introduce in this section. 
> You can connect a local repository to an empty remote one using `git remote add origin URL_OF_REMOTE`.
{: .callout}


# Exploring a Repository

Now, let's **change to our code directory** and look at the files we just downloaded.

~~~
$ cd ~/climate-analysis
$ ls
~~~
{: .language-bash}

~~~
climate_analysis.py  temp_conversion.py
~~~
{: .output}

These are some Python files for analysing climate data-
you'll recognise them if you've done some of our earlier lessons.
Don't worry, you don't need to know Python to follow along.

You'll notice that even though this directory is a **version control repository**, nothing actually looks special about it. But, if we add the `-a` flag to show everything,
we can see that there's a hidden directory called `.git`:

~~~
$ ls -a
~~~
{: .language-bash}

~~~
.  ..  climate_analysis.py  .git  temp_conversion.py
~~~
{: .output}

Git stores information about the project in here.
If we ever delete it, we will lose the project's history.

### Check Status

We can check that everything is set up correctly
by asking Git to tell us the status of our project with the **status** command:

~~~
$ git status
~~~
{: .language-bash}

~~~
git status
On branch main
Your branch is up-to-date with 'origin/main'.

nothing to commit, working tree clean
~~~
{: .output}

A **branch** is an independent line of development.  We have only one, and the default name is **main**.

Our **local repository** is connected to a **remote repository** (called **origin** by default), and is currently up-to-date; we haven't made any changes to the code yet.

Git works on **commits** - snapshots of the current state of the repository. *"nothing to commit, working tree clean"* means that the directory currently looks exactly the same as the last snapshot we took of it, with no changes or edits.

> ## Branch names
> 
> In this workshop, we have a **default branch** called **main**. In older versions of Git,
> if you create a new repository on the command line, it'll have a default branch called **master**, and a lot of examples online will show **master** instead of **main**. Don't worry - branches work the same, regardless of what they're called!
{: .callout}

{% include links.md %}
