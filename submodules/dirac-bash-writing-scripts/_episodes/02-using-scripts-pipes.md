---
title: "Using Bash Scripts in Pipes"
slug: dirac-bash-writing-scripts-using-bash-scripts-pipes
teaching: 25 
exercises: 10
questions:
- "Can I use scripts I write in pipes as well?"
objectives:
- "Use a Bash script we've written within a pipe."
- "Create a Bash script that reads input from other commands within a pipe."
keypoints:
- "You can include your own Bash scripts in pipes."
- "A common and useful pattern in Bash shell is to run a program or script that generates potentially a lot of output, then use pipes to filter out what you're really after."
---

As we've seen in a previous lesson, one of the great things about shells like Bash is that you can chain commands together using pipes, but what about our own scripts?


## Using our own Scripts in Pipes

We've already seen how we can compose commands together using pipes, like so:

~~~
$ ls | head -5 | tail -2
~~~
{: .language-bash}

So what about our own scripts? The good news is that we can use scripts we write in pipes as well, chaining together sequences of commands using them too. And this emphasises a key strength of shells like Bash: the ability to compose simple programs together to accomplish complex tasks.

This simple idea is why systems like Unix - and its successors like Linux - have been so successful. Instead of creating enormous programs that try to do many different things, Unix programmers focus on creating lots of simple tools that each do one job well, and that work well with each other.

So taking our `my_functions.sh` script, we can use it in a pipe as we would any other command:

~~~
$ ./my_functions.sh | head -10
~~~
{: .language-bash}

~~~
09:48:45
09:48:48
09:48:51
09:48:54
09:48:57
~~~
{: .output}

After printing out five lines of output, the pipe terminates.

## Accepting Input into Our Script

Oue previous example shows how we can include the output from our commands within a pipe. But what about how we might process input with our script? We can do this using `read` in Bash. Write a new script called `filter.sh`:

~~~
#!/bin/bash

while read line
do
   echo $line | grep "0$"
done
~~~
{: .language-bash}

What this script will do is continually read input using `read` until there is none left, at which point the script ends. For each line of input, we use `echo` and `grep` within a pipe to only filter out and only print any output that has `0` as the last character. The `$` in the `grep` search string means match on end of line, hence `0$` means match any string that ends with `0`.

Then set its execute permissions, and execute it within a pipe like so:

~~~
$ chmod x+ filter.sh
$ ./my_functions.sh | ./filter.sh | head -n 2
~~~
{: .language-bash}

~~~
10:49:30
10:50:00
~~~
{: .output}

Note that this pattern is quite a common one with the Bash shell: we're running a program that gives us potentially a lot of output, and we're filtering out just what we're interested in.

> ## Simple is Good
> 
> Wherever possible, we should always try to simplify the code we write, removing any extraneous use of scripts or code that isn't needed. This enhances readability and makes our code easier to understand.
> 
> We've written a script that filters out output that ends in `0`. Instead of using `./filter.sh` in our pipe, what could we replace it with that would accomplish the same thing?
> 
> > ## Solution
> > 
> > ~~~
> > $ ./my_functions.sh | grep "0$" | head -n 2
> > ~~~
> > {: .language-bash}
> > 
> > By using the `grep` directly in the pipe, we've removed the need for a separate script, simplifying the pipe.
> {: .solution}
{: .challenge}
