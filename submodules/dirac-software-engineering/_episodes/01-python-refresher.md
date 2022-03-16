---
title: "An Introduction to Python"
slug: dirac-software-engineering-brief-intro-python
teaching: 0
exercises: 0
questions:
- "Key question (FIXME)"
objectives:
- "An introduction to Python, or a reminder of key features if you've used it before."
keypoints:
- "First key point. Brief Answer to questions. (FIXME)"
---

## Data Types

- `int`
- `float`
- `str`

## Data Structures

- `list`
- `dict`

## Looping and Branching

- `if`
- `for`
- `range`

~~~ python
import random

total = 1000000
inside = 0

for i in range(total):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    r2 = x**2 + y**2

    if r2 <= 1:
        inside += 1

pi = 4 * inside / total
print(pi)
~~~
{: .language-python}

~~~
3.138856
~~~
{: .output}


## Functions

- `def`
- default parameters
- docstrings

~~~ python
import random

def approximate_pi(num_points=1000000):
    """Monte-carlo approximation of pi by counting points within a circle."""
    inside = 0

    for i in range(num_points):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        r2 = x**2 + y**2

        if r2 <= 1:
            inside += 1

    return = 4 * inside / num_points

pi = approximate_pi()
print(pi)
~~~
{: .language-python}

~~~
3.142464
~~~
{: .output}

## Python for Data

- `numpy.array`
- `pandas.DataFrame`

> ## Sum of Squares
> 
> Write a function which accepts an integer and returns the sum of the squares of integers up to **and including** this number.
> 
> > ## Solution
> > 
> > ~~~ python
> > def sum_of_squares(limit):
> >     total = 0
> >     for i in range(limit + 1):
> >         total += i * i
> > 
> >     return total
> > ~~~
> > {: .language-python}
> {: .solution}
{: .challenge}


{% include links.md %}
