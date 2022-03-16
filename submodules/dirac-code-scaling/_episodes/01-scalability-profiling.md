---
title: "Scalability Profiling"
slug: dirac-code-scaling-scalability-profiling
teaching: 0
exercises: 0
questions:
- "How scalable is a particular piece of code?"
- "How can I generate evidence for a particular code's scalability?"
- "What does good and bad scalability look like?"
objectives:
- "Explain how Amdahl's Law can help us understand the scalability of code"
- "Use Amdahl's Law to predict the theoretical maximum speedup on some example code when using multiple processors"
- "Understand strong and weak scaling graphs for some example code"
- "Describe the graphing characteristics of good and bad scalability"
keypoints:
- "We can use Amdahl's Law to understand the expected speedup of a parallelised program against multiple cores."
- "It's often difficult to estimate the proportion of serial code in our programs, but a reformulation of Amdahl's Law can give us this based on multiple runs against a different number of cores."
- "Run timings for serial code can vary due to a number of factors such as overall system load and accessing shared resources such as bulk storage."
- "The Message Passing Interface (MPI) standard is a common way to parallelise code and is available on many platforms and HPC systems, including DiRAC."
- "When calculating a *strong scaling* profile, the additional benefit of adding cores decreases as the number of cores increases."
- "The limitation of strong scaling is the fixed problem size, and we can increase the problem size with the core count to obtain a *weak scaling* profile."
---

Let's look at how we can determine the scalability characteristics for some example code.

## Pi as a Code Example

In the following example we have a simple piece of code that calculates pi. When run on our local system using MPI we get the following results:

| Cores (n) | Run Time (s) | Result      | Error         | Speedup |
|-----------|--------------|-------------|---------------|---------|
| 1         | 3.99667      | 3.141592655 | 0.00000003182 |         |
| 2         | 2.064242     | 3.141592655 | 0.00000003182 | 1.94    |
| 4         | 1.075068     | 3.141592655 | 0.00000003182 | 3.72    |
| 8         | 0.687097     | 3.141592655 | 0.00000003182 | 5.82    |
| 16        | 0.349366     | 3.141592655 | 0.00000003182 | 11.44   |

You see that we can reduce the run time of our code by using more cores without affecting the results.

> ## What Type of Scaling?
>
> Looking at the figures above, is this an example of strong or weak scaling?
>
> > ## Solution
> >
> > This is an example of strong scaling, as we are keeping the data sample the same but increasing the number of cores used.
> {: .solution}
{: .challenge}

When these results are plotted we see the following graph:

<img alt="Time vs Cores for an implementation of Pi" src="../fig/scalability-pi-time-vs-cores.png" width="600" />

This gives us a good indication of the code's strong scaling profile. As you can see, the benefit of using cores reduces as they increase, which is due to the serial portion of our code. Our example code it is made up mostly of computation that is parallelised, but we still have and require sections of code to declare variables, initialise various aspects of our code and environment which includes MPI, and gather the results.

> ## How are we Parallelising our Pi Program Across Multiple Cores?
> 
> Our pi program uses the commonly used [Message Passing Interface (MPI)](https://en.wikipedia.org/wiki/Message_Passing_Interface) standard to enable communication between each of the parallel portions of code running on separate cores. It's been around since the mid-1990's, is widely available on many operating systems, and is designed to make use of multiple cores on a variety of platforms from a multi-core laptop to large-scale HPC resources such as those available on DiRAC. There are many available [tutorials](https://hpc-tutorials.llnl.gov/mpi/) on MPI.
{: .callout}

The speedup shown in the table above was calculated using:

> *Speedup = T<sub>1</sub> / T<sub>n</sub>*

## Determining Serial and Parallel Proportions of Code

We can use [Amdahl's Law](https://en.wikipedia.org/wiki/Amdahl%27s_law) to give us an indication of the speedup of adding more cores when running our code. In order to do this, we need an idea of what proportions of our code are serial and parallel.

It is sometimes difficult to estimate the proportion of serial code, but we can estimate this using Amdahl's Law.

Assuming:
> *Time to Complete (T) = Time taken for Serial Portion (S) + Time taken for Parallel portion (P)*
> 
> *T = S + P*

To help us solve this we can write the parallel position P as T - S. this gives us:

> *T = S + ( T - S )*

Assuming for simplicity that the serial portion is constant and that only the parallel portion of the code is affected when we increase the number of cores available. Using 2 cores we can rewrite Amdahl's law as such:

> *T<sub>2</sub> = S + ( T<sub>1</sub> - S ) / 2*

When using n cores we get:

> *T<sub>n</sub> = S + ( T<sub>1</sub> - S ) / n*

We can now rearrange this to solve for S the time taken for the serial portion of our code.

> S = ( nT<sub>n</sub> - T<sub>1</sub> ) / (n - 1)

Using the above formula on our example code we get the following results:

| Cores (n) | T<sub>n</sub> | S            | (T - S) = P | Serial % | Parallel % |
|-----------|---------------|--------------|-------------|----------|----------|
| 1         | 3.99667       |              |             |          |          |
| 2         |               | 0.131814     | 3.864856    | 3.30     | 96.706   |
| 4         |               | 0.1012006667 | 3.895469333 | 2.53     | 97.47    |
| 8         |               | 0.2143008571 | 3.782369143 | 5.36     | 94.64    |
| 16        |               | 0.1062124    | 3.8904576   | 2.66     | 97.34    |
|-----------|---------------|--------------|-------------|----------|----------|
|           |               |              | Average     | 3.46     | 96.54    |

As you can see, we now have an estimated percentage for our serial and parallel portion of our code.

> ## Why the Odd Differences in Serial Timings?
> 
> You may have been wondering why serial code seems to vary depending on the run. There are several factors that are impacting our code. Firstly these were run on a working system with other users, so runtime will be affected depending on the load of our systems. Throughout DiRAC it is normal when you run your production code on our system to have exclusive access to the servers, so this will be less of an issue, but if your code accesses our bulk storage then there may be an impact as these are shared resources with other users. As we are using the MPI library in our code it would be expected that the serial portion will actually increase slightly with the number of cores. This will have a real impact when you start scaling your code into thousands of cores.
{: .callout}

## What's the Maximum Speedup?

We can now use these figures to give us the theoretical maximum possible speed up we could achieve:

> *Speedup = T<sub>1</sub>/T<sub>n</sub>*

And

> *T<sub>n</sub> = S + (T<sub>1</sub> - S) / n*

For simplicity and when using percentages we normally set *T<sub>1</sub>* to 1. Therefore we will get a speedup fact relative to 1.

Therefore:

> *Speedup = 1 / T<sub>n</sub>*
> 
> *T<sub>n</sub> = S + ( 1 - S ) / n*

As we increase the number of cores to infinity, then *T<sub>n</sub>* approaches *S*.

> *T<sub>n</sub> = S*
> 
> *Max Speedup = 1 / S *

And in our case:

> *Max Speedup = 1 / 4% => 25*

> ## Number of Cores vs Expected Speedup
> 
> Using Amdahl's Law and the percentages of serial and parallel proportions of our example code. Fill In or create a table estimating the expected total speedup and change in speedup when doubling the number of cores, in a table like the following (with the number of cores doubling each time until a total of 4096):
>
> | Cores (n) | T<sub>n</sub> | Speedup | Change in Speedup |
> |---------------|-----------|---------------|-------------------|
> | 1         | 3.99667       |         |                   |
> | 2         |               |         |                   |
> | 4         |               |         |                   |
> | ...         |               |         |                   |
> | 4096         |               |         |                   |
> 
> > ## Solution
> > Hopefully from your results you will find that we can get close to the maximum speedup of 25, but it requires ever more resources.
> {: .solution}
{: .challenge}

> ## Speedup Change?
> 
> When does the change in speedup drop below 1%?
> 
> > ## Solution
> > From our own trial runs this happens at 4096 core, but it is expected that we would never run this code at these core counts as it would be a waste of resources.
> {: .solution}
{: .challenge}

> ## How Many Cores Should we Use?
>
> From the data you have just calculated, what do you think the maximum number of cores we should use with our code to balance reduced execution time versus efficient usage of compute resources.?
> 
> > ## Solution
> > 
> > Within DiRAC we do not impose such a limit, this would be a decision made by the researchers. Every project has an allocation and it is up to you to decide what is efficient use of your allocation. In this case I personally would not waste my allocation on any runs over 128 cores.
> {: .solution}
{: .challenge}


## Calculating a Weak Scaling Profile

Not all codes are suited to strong scaling. As seen in the previous example, even codes with as much as 96% parallelizable code will hit limits. Can we do something to enable moderately parallelizable codes to access the power of our HPC systems? The answer is yes, and is known as *weak scaling*.

The problem with strong scaling is as we increase the number of cores then the relative size of the parallel prison of our task reduces until it is negligible, and then we can not go any further. The solution is to increase the problem size as you increase the core count. This method tries to keep the proportion of serial time and parallel time the same. We will not get the benefit of reduced time for our calculation, but we will have the benefit of processing more data. Below is a rerun of our Ii code, but this time as we increase the core we also increase the samples used to calculate Pi.

| Cores (n) | Run Time | Result       | Error         | % Improved Error |
|-----------|----------|--------------|---------------|------------------|
| 1         | 4.149807 | 3.141592655  | 0.00000003182 |                  |
| 2         | 4.362416 | 3.141592654  | 0.00000001591 | 50.00%           |
| 4         | 5.205988 | 3.141592654  | 0.00000000795 | 75.02%           |
| 8         | 4.356564 | 3.141592654  | 0.00000000397 | 87.52%           | 
| 16        | 4.643724 | 3.141592654  | 0.00000000198 | 93.78%           |

<img alt="%Improved Error vs Cores" src="../fig/scalability-improved-error-vs-cores.png" width="600" />

As you can see, the time to complete is similar, just slightly increasing. However, the accuracy to calculate Pi has increased. In fact our % improvement is nearly in step with the number of cores.

When presenting your weak scaling it is common to show how well it scales, this is shown below:

<img alt="Weak Scaling - Cores vs Time" src="../fig/scalability-weak-scaling-time.png" width="600" />

We can also plot the scaling factor. This is the percentage increase in run time compared to base run time for a normal run. In this case we are just using *T<sub>1</sub>*:

<img alt="Weak Scaling - Cores vs Scaling Factor" src="../fig/scalability-weak-scaling-factor.png" width="600" />

As you can see from our plot, the code is highly scalable. We do have an anomaly with our 4 core run, however. It would be good to rerun this to get a more representative sample, but this result is a common occurence when using shared systems. In this example we only did a single run, but when compiling your data for presentation or submitting applications it would be better to do many runs and exclude outlining data samples or provide an uncertainty estimate.

> ## Maximum Cores to Use?
> 
> It would be hard to estimate the max cores we could use from this plot. Can you suggest an approach to get a clearer picture of this code's weak scaling profile?
> 
> > ## Solution
> >
> > The obvious answer is to do more runs at high core counts, and try to resolve the C4 sample. This should give you a clearer picture of the weak scaling profile.
> {: .solution}
{: .challenge}

> ## Obtaining Resources to Profile your Code
> 
> It may be difficult to profile your code if you do not have the resources at hand, but DiRAC can help. If you are in a position of wanting to use DiRACs facilities but do not have the resources to profile your code, then you can apply for a [Seedcorn project](https://dirac.ac.uk/seedcorn/). This is a short project with up to 100,000 core hours for you to profile and possibly improve your code before applying for a large allocation of time on our facilities.
{: .callout}

> ## Profiling Pi Yourself
> 
> If you would like to reproduce these sample runs on your system, the code is available on the DiRAC GitHub page.
{: .callout}


{% include links.md %}
