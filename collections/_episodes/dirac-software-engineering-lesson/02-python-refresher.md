---
title: "An Introduction to Python"
slug: dirac-software-engineering-brief-intro-python
teaching: 15
exercises: 15
questions:
- "What are the key parts of Python we'll need to know for the rest of the material?"
objectives:
- "An introduction to Python, or a reminder of key features if you've used it before."
keypoints:
- "We'll be using Python for the following parts of the material, here's an introduction / refresher."
---

Python is one of the most popular languages in research computing, so even if it's not the main language you use, it's worth knowing about.
This makes it a good choice of language for teaching purposes, so we're going to use Python for most of the examples for the remainder of this course.

Before we can move on though, we'll cover some of the core features of Python here.
If you're already familiar with Python, consider this a refresher.
If not, then this section should cover everything you need to know for the remainder.

## Data Types

An obvious place to start when learning a new language is with how it stores and represents data.
In most languages, there are a range of **types** of data which can be represented.
In Python, the most fundamental types are:

- Integers - `int`
- Floating point numbers - `float`
- Booleans - `bool`
- Strings - `str`

We create a **variable** and assign a value to it using the `=` operator.

``` python
int_variable = 5
float_variable = 3.142
bool_variable = True
str_variable = "Hello world!"

print(int_variable)
print(float_variable)
print(bool_variable)
print(str_variable)
```
{: .language-python}

Unlike some other languages (e.g. C, C++, Fortran, Java), we don't need to say what data type a variable is going to hold - a variable can actually hold different types over its lifetime, e.g.:

``` python
my_var = 5
my_var = "Hello world!"

print(my_var)
```
{: .language-python}

```
Hello world!
```
{: .output}

Also unlike these languages, there's no way in Python to **declare** a variable without assigning to it.

## Data Structures

But what about when we need to store more than one value?
That's where the next set of types comes in, the **collection** types, representing common **data structures**.
These data structures are:

- `list`
- `dict`
- `set`

Let's start with lists.
A list is a sequence of values - it has an order and particular values can be accessed based on their position within the list.
Like many other languages, we start counting positions at 0, so the first item in a list is "item 0", the second is "item 1", and so on.
If we need to add a new value to the end of an existing list we can use the `append` function / method.

``` python
odd_numbers = [1, 3, 5, 7, 9]
odd_numbers.append(11)

print(odd_numbers)
print(odd_numbers[3])
```
{: .language-python}

```
[1, 3, 5, 7, 9, 11]
7
```
{: .output}

For much more information on lists, see https://docs.python.org/3/tutorial/datastructures.html#more-on-lists.

**Dictionaries** are the second type of collection, typically used to associate a key and a value - like the index of a book:

``` python
index = {
    "python": 1,
    "c++": 5,
    "fortran: 5,
}

index["java"] = 12
print(index["c++"])
```
{: .language-python}

```
2
```
{: .output}

In a dictionary, a key can only be present once, so in the example above we couldn't for example:

``` python
index = {
    "python": 1,
    "python": 2,
    "c++": 5,
    "fortran": 5,
}
```
{: .language-python}

In this case, the value at the key `"python"` will have the last value we provided for it: `2`.

The final collection type we'll introduce here is a **set**.
Sets are similar to dictionaries, but 


## Looping and Branching

Now we know how to store and structure data, let's move onto processing that data.
Two important ideas in most programming languages you'll encounter are branching and looping.
In Python we use these two keywords:

- `if`
- `for`

``` python
number = 53

if number > 50:
    print("Number was greater than 50")
```
{: .language-python}

~~~
Number was greater than 50
~~~
{: .output}

In the example above, because `number` is greater than 50, the **condition** evaluates as `True` and the **block** of code within the `if` is executed.
Code blocks are introduced in Python with a colon (`:`), which we see in the example above, but we'll also see in a couple of other contexts soon.
If the condition doesn't evaluate as `True` (i.e. it evaluates as `False`), the block of code is skipped.

We can also add more possible outcomes to the branching using `elif` (short for "else if") and `else`.
With `elif` we provide another condition and the block of code we provide executes if all of the previous conditions evaluate as `False`, but this one evaluates as `True`.
If none of the conditions evaluate as `True`, then the `else` block executes.

Both `elif` and `else` are optional - you can have zero or more `elif` blocks and zero or one `else` blocks.

~~~ python
number = 94

if number > 100:
    print("Greater than 100")
elif number == 100:
    print("Equal to 100")
else:
    print("Less than 100")
~~~
{: .language-python}

~~~
Less than 100
~~~
{: .output}

Loops are another important construct, which in Python use the keyword `for`:

~~~ python
fruit_bowl = ["apple", "banana", "cherry"]

for fruit in fruit_bowl:
    print(fruit)
~~~
{: .language-python}

~~~
apple
banana
cherry
~~~
{: .output}

In the example above, we loop over a collection.
Each time the loop executes, the variable `fruit` takes the value of the next item from the collection.

Another common way to use loops is with the `range()` **function**.
This function takes **arguments** for the bounds and produces a sequence of integers ranging from the lower bound to the upper bound.

~~~ python
for i in range(10):
    print(i)
~~~
{: .language-python}

~~~
0
1
2
3
4
5
6
7
8
9
~~~
{: .output}

In the above example, we just provide an upper bound, the lower bound takes the default value of 0.
Notice that the values include the lower bound, but exclude the upper bound - this matches the zero-based indexing of lists.

So let's take these and do something useful.
One relatively simple numerical model is the approximation of pi, using a Monte Carlo method.

If we generate a large number of points random uniformly distributed within a square, the proportion of these points which are also within a circle of the same diameter gives us an approximation of pi, via the formula for the area of a circle:

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

We've actually now got everything we need to write any program, but if we stopped here we'd quickly find that larger programs become unmanageable.
What we're missing is a way of structuring our code, so that we can separate out specific parts with specific functionality.
The first and most important tool for doing this are **functions**.

Much like in mathematics, functions represent an operation which can be applied to some data, to receive some other data as output.

~~~ python
def add_one(x):
    """Add one to a number."""
    return x + 1

print(add_one(3))
~~~
{: .language-python}

~~~
4
~~~
{: .output}

In the example above, we define a function `add_one` which adds one to a number.
To define a function, we need to start with the `def` keyword, then the function name, the function **arguments** in parentheses and the colon to start a new block.
Within the function's code block we can do anything we could outside of a function, but in order to get any data back out of the function we need to `return` it.

The arguments of a function are the values it takes as input - when we **call** the function inside the `print()`, we provide the values of any required parameters, in this case just `x`.
The value returned by the function is then passed on to `print()`, just as it would be if we'd put the value there directly.

The last component of the function definition above is the **docstring**.
Docstrings aren't a requirement, but can make it much easier to understand what your code is doing, especially if it's complex or you haven't looked at it for a while.
A docstring needs to be the first thing inside a function's code block and should be enclosed within triple double quotes (i.e. `"""`).

> ## A Function for Pi
>
> Take our existing example for the Monte Carlo approximation of pi and convert it into a function.
>
> > ## Solution
> > 
> > ~~~ python
> > import random
> >
> > def approximate_pi(num_points=1000000):
> >     """Monte-carlo approximation of pi by counting points within a circle."""
> >     inside = 0
> > 
> >     for i in range(num_points):
> >         x = random.uniform(-1, 1)
> >         y = random.uniform(-1, 1)
> > 
> >         r2 = x**2 + y**2
> > 
> >         if r2 <= 1:
> >             inside += 1
> > 
> >     return = 4 * inside / num_points
> > 
> > pi = approximate_pi()
> > print(pi)
> > ~~~
> > {: .language-python}
> > 
> > ~~~
> > 3.142464
> > ~~~
> > {: .output}
> >
> > In this example solution, we've provided a default value for the number of points, meaning that when someone calls the function they may choose not to specify how many points, in which case the default value will be used.
> {: .solution}
{: .challenge}

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
