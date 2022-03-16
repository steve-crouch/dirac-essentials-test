---
title: "Understanding Code Scalability"
slug: dirac-code-scaling-understanding-code-scalability
teaching: 0
exercises: 0
questions:
- "What is code scalability?"
- "Why is code scalability important?"
- "How can I measure how long code takes to run?"
objectives:
- "Describe why code scalability is important when using HPC resources"
- "Explain the difference between walltime and computational time"
- "Describe the differences between strong and weak scaling"
- "Summarise the dangers of premature optimisation"
keypoints:
- "To make efficient use of parallel computing resources, code needs to be scalable."
- "Before using new code on DiRAC, it's strong and weak scalability profiles have to be measured."
- "Strong scaling is concerned with how the solution time varies with the number of processors for a fixed overall problem size."
- "Weak scaling is concerned with how the solution time varies with the number of processors for a fixed problem size for each processor."
- "Strong and weak scaling measurements provide good indications for how jobs should be configured to use resources."
- "Always profile your code to determine bottlenecks before attempting any non-trivial optimisations."
---

When we submit a job to a cluster that runs our code, we have the option of specifying the number of CPUs (and in some cases GPUs) that will be allocated to the job. So we also need to consider to what extent that code is *scalable* with regards to how it uses these resources, to avoid the risk of code consuming more resources than it can effectively use.

As part of the application process for having new code installed on DiRAC, its scalability characteristics need to be measured. This thus helps inform how best to assign CPU resources when configuring jobs to run with that code.

There are two primary measures of execution time we need to consider for any given code:

- *Wall clock time (or actual time)* - this is the time it takes to run from start of execution to the end. In terms of scaling meaurements, this does not include any time waiting in a scheduler for the job to start.
- *Computational time* - this is the time actually spent running your code on a CPU. In some cases where you are running on a system which is shared by other users, then your run may be swapped out to enable other users to use the system. Most systems within DiRAC are configured to have exclusive access. So your code will not be competing with other programs on the compute nodes, but may be competing on the network fabric, or for storage bandwidth.

## How can we Characterise a Code's Scalability?

So before we consider running and using code on an HPC resource, we need to understand it's *scaling profile* - so we can determine how the code will scale as we add more cores to running it. That way, when we run code we can request a suitable amount of resources with minimal waste. There are two types of scaling profile wew need to determine:

- **Strong scaling:** During the process of determining how well you code scales you can determine the code's strong scaling profile. This is done by keeping the problem size constant, and then increasing the number of cores (and nodes) used. The resulting data can then be plotted. Ideally, a 100% scalable application will have a profile that halves the time to complete when given twice as many cores. This is rarely met as most real world applications have some serial portion which will limit the code's scalability.
- **Weak scaling:** This is similar to strong scaling, but in this case as we increase the number of cores, we also increase the problem size by the same factor. This type of scaling is more easily met, and should result in a flat line plot if the code has good weak scaling characteristics. In theory this removes the impact of the serial portion of your code, but in reality there is still a limit.

Once we understand these profiles, we'll have an idea of the **speedup** of the code using multiple cores - the improvement in speed of execution of a task executed on two similar architectures with different resources. These measurements give us good indications for how jobs for this code should be specified, in terms of overall job size and the amount of resources that should be requested.

## I'm a Developer, Should I Optimise the Code?

As a developer if your code happens to take too long to run or scales badly it's tempting to try to optimise it straight away. But before you do, consider the following [three rules of optimisation](https://wiki.c2.com/?RulesOfOptimization):

- **1.** Don't
- **2.** Don't *yet*, and
- **3.** If you must optimise your code, *profile* it before optimising

In non-trivial cases premature optimisation is regarded as bad practice, since optimisation may lead to added code complexity and reduced readability, making the code harder to understand and maintain over time. It is often effort-intensive, and also it's also difficult at a low level, particularly with modern compilers and interpreters, to improve on or anticipate the optimisations they will use. A general maxim is to focus on writing understandable code and getting things working first - the former helps with the latter. Then, once strong and weak scaling profiles have been measured, if optimisation is justifieid you can *profile* your code to work out where and how best to optimise it.

So what is *code profiling*? Profiling your code is about understanding its complexity and performance characteristics, with the usual intent to work out how best to *optimise* the code to improve its performance in some way - typically in terms of speedup, memory, or disk usage. In particular, profiling helps identify *where* bottlenecks exist in the code for these aspects, avoiding summary judgements and guesses which often lead to unnecessary optimisations.

> ## Profilers
>
> Each programming language typically offers some open-source and/or free tools
> on the web, with which you can profile your code. Here are some examples of
> tools. Note though, depending on the nature of the language of choice, the
> results can be hard or easy to interpret. In the following we will only list
> open and free tools:
>
> - Python: [line_profiler](https://github.com/pyutils/line_profiler),
>   [prof](https://docs.python.org/3.9/library/profile.html)
> - JavaScript: [firebug](https://github.com/firebug/firebug)
> - Ruby: [ruby-prof](https://github.com/ruby-prof/ruby-prof)
> - C/C++: [xray](https://llvm.org/docs/XRay.html),
>   [perf](https://perf.wiki.kernel.org/index.php/Main_Page),
> - R: [profvis](https://github.com/rstudio/profvis)
{: .callout }

Donald Knuth said *"We should forget about small efficiencies, say about 97% of the time: premature optimization is the root of all evil. Yet we should not pass up our opportunities in that critical 3%."*. So in short, optimise the obvious trivial, but avoid non-trivial optimisations until you've understood what needs to change - optimisation is often expensive in terms of time!


{% include links.md %}
