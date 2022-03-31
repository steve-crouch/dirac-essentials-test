---
title: "Remote Repositories"
slug: dirac-version-control-remote
teaching: 10
exercises: 0
questions:
- "How do I work with a remote repository?"
objectives:
- "Add an SSH key to a GitHub account"
- "Understand `git push` and `git pull`"
keypoints:
- "Git can easily synchronise your local repository with a remote one"
- "GitHub needs an SSH key to allow access"
---

We've learned how to use a **local repository** to store our code and view changes:

![Local Repository Commands]({{ site.url }}{{ site.baseurl }}/fig/05-remote/local.png){:width="60%"}

Now, however, we'd like to share the changes we've made to our code with others, as well as making sure we have an off-site backup in case things go wrong. We need to upload our changes in our **local repository** to a **remote repository**.

> ## Why Have an Off-site Backup?
>
> You might wonder why having an off-site backup (i.e. a copy not stored at your University) is so important. In 2005, [a fire destroyed a building at the University of Southampton](http://news.bbc.co.uk/1/hi/england/hampshire/4390048.stm). Some people's *entire PhD projects* were wiped out in the blaze. To ensure your PhD only involves a normal level of suffering, please make sure you have off-site backups of as much of your work as possible!
>
{: .callout}

## Setting Up GitHub

To do that, we'll use the **remote repository** we set up on GitHub at the start of the workshop. It's another repository, just like the **local repository** on your computer, that Git makes it easy to send and receive data from. Multiple **local repositories** can connect to the same **remote repository**, allowing you to collaborate with colleagues easily.

![Remote Repositories]({{ site.url }}{{ site.baseurl }}/fig/05-remote/remote.svg){:width="60%"}

So we're finally going to address all those *"Your branch is ahead of 'origin/main' by 3 commits"* messages we got from `git status`! However, GitHub doesn't let just anyone push to your repository - you need to prove you're the owner (or have been given access). As constantly re-entering a password is inconvenient and insecure, we'll set up an SSH key to authenticate our identity. 

We should already have one in order to access  the DIRAC cluster, so we just need to head [back to GitHub](https://github.com) and register the key there. Go to [GitHub > Settings > SSH and GPG keys > Add new](https://github.com/settings/ssh/new), and you should see this:

![Add New SSH Key]({{ site.url }}{{ site.baseurl }}/fig/05-remote/ssh.png)

We need to fill in the details. Give the key a title like "DIRAC SSH key", and then paste your **public key** into the key box - we can find it in our `~/.ssh` folder:

~~~
$ ls ~/.ssh
~~~
{: .language-bash}

~~~
config id_rsa  id_rsa.pub  known_hosts
~~~
{: .output}

You might have more SSH keys, or differently-named ones. You want to copy the contents of the `.pub` file you used for your DIRAC account into the key box, e.g.:

~~~
$ cat ~/.ssh/id_rsa.pub
~~~
{: .language-bash}

~~~
<SNIPPED FOR SECURITY>
~~~
{: .output}

**Make sure you copy the `.pub` file and not the private key!** Your private key lives on your machine and is never shared with anyone else.

Then click **Add key**, and you're sorted - you should be able to send your changes to GitHub, so let's go into how.

## Updating a Remote Repository

* Finally going to send our data to the remote repository we set up earlier
* `git push`
* Reload the webpage and see

## Updating a Local Repository

* Example of working with collaborators
* Edit the README.md file on GitHub, commit directly to main
  * Point out that this isn't common but just an example
* Edit climate_analysis.py locally
* `git push`, see an error
* `git pull` to update
* `git push`
* You can use branches to mitigate these issues, each new feature has its own branch
* Merge conflicts can happen (not in the outline for this course)

![Remote Repository Commands]({{ site.url }}{{ site.baseurl }}/fig/05-remote/remote.png){:width="60%"}

{% include links.md %}
