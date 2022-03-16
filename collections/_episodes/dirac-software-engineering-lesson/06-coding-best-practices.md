---
title: "Best Practices in Writing Code"
slug: dirac-software-engineering-best-practices-writing-code
teaching: 0
exercises: 0
questions:
- "How do I write code to ensure that others, including myself, will be able to continue to understand it?"
- "What can I do to ensure my code can be used, modified and extended in the future?"
objectives:
- "Explain the benefits of writing readable code."
- "Describe the importance of clear code indentation, formatting, and naming."
- "List examples of things that should and should not be code commented."
- "Explain why conforming to defined coding conventions is beneficial."
- "Explain benefits of writing maintainable code."
- "Describe what is meant by *technical debt*."
- "Understand approaches for writing maintainable code."
- "Describe questions that can be used as a checklist for whether code is maintainable."
keypoints:
- "Source code is designed for humans, not machines."
- "Source code is read much more often than it is written."
- "Always assume that someone else will read your code at a later date, including yourself."
- "Good indentation greatly enhances code readability."
- "Name things like variables, functions, and modules to indicate purpose."
- "Good comments describe the reasons behind coding approaches as well as complex behaviour."
- "Community coding conventions help you create more readable software projects that are easier to contribute
  to."
- "Maintainable code is easier to understand, modify, extend, and fix."
- "Assume any piece of code you write will be reused."
- "*Technical debt* is incurred when quick solutions are prioritised over good solutions, but is paid off in the cost of maintaining the code."
- "Change the way you write code to make maintainability a key goal."
---

## Writing Readable Source Code

Source code is designed for humans. It may end up being processed by a machine, but it evolves in our hands and we need to understand what the code does and where changes need to be made. We may understand our code now, but what about six months or a year from now? Readable code helps us to re-aquaint ourselves with what we wrote and why we wrote it.

Our code may embody some unique aspect of our research. Readable code can help our fellow researchers to understand what we've done and so to assess whether this aspect of our research is correct. Or, to put it another way, would we rather have a colleague spot a problem now, or, six months later when we've published a paper based on flawed results produced using our software?

There's also our image to consider. If our code is badly laid out, messy and cryptic, others will assume that it is also buggy and sloppily written. They may assume that we undertake our research in a similarly slack manner.

If we're working in a team to develop some code then readable source code can ensure that everyone can understand the code written by everyone else. This can help improve a team's **bus factor**, which is defined as the number of developers who need to be put out of action before noone understands the code.

Writing readable code costs only a little more time than writing unreadable code, but the payback is immense. Reading and understanding source code is slow, laborious and can lead to misinterpretation. It is always a good idea to keep others in mind when writing code, so a good rule of thumb is to assume that someone will always read your code at a later date, and this includes a future version of yourself!

### Code Formatting

The formatting or appearance of code determines how quickly and easily the reader can understand what it does. A compiler will see no difference between this...

~~~
// Example 1: unformatted code.
public class Functions
{
public static int fibonacci(int n)
{
if (n < 2)
{
return 1;
}
return fibonacci(n-2) + fibonacci(n-1);
}

public static void main(String[] arguments)
{
for(int i=0;i<10;i++)
{
print(“Input value:”+i+” Output value:”+power(fibonacci(i), 2)+1);
}
}
}
~~~
{: .language-c}

...and this...

~~~
// Example 2: formatted code.

public class Functions
{
    public static int fibonacci(int n)
    {
        if (n < 2)
        {
            return 1;
        }
        return fibonacci(n-2) + fibonacci(n-1);
    }

    public static void main(String[] arguments)
    {
        for (int i = 0; i < 10; i++)
        {
            print(“Input value:” + i +
                  ” Output value:” +
                  power(fibonacci(i), 2) + 1);
        }
    }
}
~~~
{: .language-c}

...but the second example will be more easily understood by the reader.

Indentation makes a clear connection between blocks of code and the classes, functions or loops to which they belong. If a statement is longer than a single line on screen, indentation helps the reader understand where the statement begins and ends. White-space makes the code appear less cluttered and allows the grouping together of logically-related elements like constants or local variable declarations.

In many languages, indentation is purely cosmetic (e.g. C/C++ or Java) and the number of spaces used to indent code is left to the developer to decide. However, in certain languages (e.g. Python or Occam) indentation is more restrictive because it has semantic significance: it defines a loop body or a function body.

Many programming environments, also known as Integrated Development Environments or IDES (e.g. PyCharm, Eclipse, JBuilder, NetBeans and Microsoft Visual Studio), provide support for code formatting, and many text editors can be extended with support for language-specific indentation (e.g. Microsoft Visual Studio Code).

Good formatting can impact upon design. A function with seven arguments might not be very readable on-screen, for example. To make it more readable, you could create a new data structure or class to hold some of the arguments. We could also break up a function that cannot be viewed on one screen into a number of smaller functions that can, if the function can be logically decomposed in this way.

### Naming Things

The careful selection of names is very important to understanding. Cryptic names of components, modules, classes, functions, arguments, exceptions and variables can lead to confusion about the role that these components play. Good naming is fundamental to good design, because source code represents the most detailed version of our design. Compare and contrast the ease with which the following statements can be understood:

~~~
out(p(f(v), 2) + 1)
~~~
{: .language-python}

~~~
print(power(fibonacci(argument), 2) + 1)
~~~
{: .language-python}

There are common naming recommendations. Modules, components and classes are typically nouns (e.g. Molecule, BlackHole, DNASequence). Functions and methods are typically verbs (e.g. spliceGeneSequence, calculateOrbit). Boolean functions and methods are typically expressed as questions about properties (e.g. isStable, running, containsAtom).

Naming also relates to the use of capitalisation and delimiters, which can help a reader to quickly determine if something is a function, variable or class. For example, common guidelines for C and Java include:

- Constants should be capitalised: PI, MAXIMUM_VALUE.
- Class names should start with an initial capital with the first letter of subsequent words capitalised (this is called Camel Case): Molecule, BlackHole, DNASequence.
- Functions should start with a lower-case letter with the first letter of subsequent words capitalised: spliceGeneSequence, calculateOrbit.

Similar conventions exist for other languages.

### Code Comments

Source code tells the reader what the code does, whilst code comments allow us to provide the reader with additional information about it. The reader should be able to understand a single function or method from its code and its comments, and should not have to look elsewhere in the code for clarification. It can be easy to get lost in code, and others  will not have the same knowledge of our project or code as we do.

The kind of things that need to be commented are:

- Why certain design or implementation decisions were adopted, especially in cases where the decision may seem counter-intuitive.
- The names of any algorithms or design patterns that have been implemented.
- The expected format of input files or database schemas.

There are some restrictions. Comments that simply restate basic code behaviour line-by-line are redundant - it's better to focus comments on *why* the code is as it is, or to explain particularly complex behaviour. Of course, comments must be accurate, because an incorrect comment causes more confusion than no comment at all, so remember to update comments when you update your code!

Many languages allow you to use special types of comment to describe the functions and modules in your code, which is often a helpful discipline for increasing readability. For example, in Python these are known as *docstrings*: if the first thing in a function is a string that is not assigned to a variable, that string is attached to the function as its documentation. Consider the following code implementing a function for calculating the nth Fibonacci number:

~~~
def fibonacci(n):
    """Calculate the nth Fibonacci number.

    A recursive implementation of Fibonacci array elements.

    :param n: integer
    :raises ValueError: raised if n is less than zero
    :returns: Fibonacci number
    """
    if n < 0:
        raise ValueError('Fibonacci is not defined for N < 0')
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)
~~~~
{: .language-python}

Note here we are explicitly documenting our input variables, what is returned by the function, and also when the ValueError exception is raised. Along with a helpful description of what the function does, this information can act as a contract for readers to understand what to expect in terms of behaviour when using the function, as well as how to use it. Docstrings can also be used at the start of a Python module (a file containing a number of Python functions) or at the start of a Python class (containing a number of methods) to list their contents as a reference.

### Coding Conventions

As each language has its own syntax, semantics and sets of built-in commands, what constitutes readable code differs across programming language. What is readable is also affected by the opinions and preferences of the individual reader. Nevertheless, a number of language-specific coding conventions have evolved, reflecting both general and language-specific good practice.

It’s recommended that projects adopt a set of coding conventions or *style guide*. Not only does this promote readable code, it helps ensure that the code looks consistent, even if it the software consists of hundreds of source code files and is worked on by many developers. Projects as varied as Mozilla, Linux, Apache, GNU, and Eclipse all have their own project-specific conventions that their developers are expected to conform to. The Python language, for example, has the [PEP8](https://peps.python.org/pep-0008/) style guide.

> ## Style consistency
> 
> One of the [key insights from Guido van Rossum](https://www.python.org/dev/peps/pep-0008/#a-foolish-consistency-is-the-hobgoblin-of-little-minds) who invented the Python language, is that code is read much more often than it is written. Style guidelines are intended to improve the readability of code and make it consistent across the wide spectrum of Python code. Consistency with the style guide is important. Consistency within a project is more important.
> Consistency within one module or function is the most important. However, know when to be inconsistent --
sometimes style guide recommendations are just not applicable. When in doubt, use your best judgment.
Look at other examples and decide what looks best. And don't hesitate to ask!
{: .callout}

Project-specific conventions can also embody requirements specific to our project. They promote consistency of naming across packages, components, classes, or functions: 'All test classes must have the suffix Test, e.g. FourierUtilitiesTest'. They ensure that others know who owns the copyright on our source code: 'All source code files must have a comment with the statement Copyright © My Organisation, 2010'. They ensure that others know about restrictions on our source code: 'All source code files should have a comment with the text "Licensed under the Apache License, Version 2.0".'

Code analysis tools allow our coding conventions to be defined as rules. Our source code can then be analysed against these rules to automatically check for conformance. These tools can publish reports that highlight what rules are violated and where in the code the violations occur. Popular code analysis tools are CheckStyle for Java, StyleCop for C#, Pylint or Flake8 for Python, and codetools for R. For other languages see Wikipedia's [List of tools for static code analysis](https://en.wikipedia.org/wiki/List_of_tools_for_static_code_analysis). In addition, many IDEs such as PyCharm and VSCode are able to highlight common code convention and formatting issues as you type.


## Writing Maintainable Software

Software always needs new features or bug fixes. Maintainable software is easy to extend and fix, which encourages the software's uptake and use. Maintainable software allows you to quickly and easily:

- Fix a bug, without introducing a new bug as you do so
- Add new features, without introducing bugs as you do so
- Improve usability
- Increase performance
- Make a fix that prevents a bug from occurring in future
- Make changes to support new environments, operating systems or tools
- Bring new developers on board your project

More formally, the IEEE Standard Glossary of Software Engineering Terminology defines maintainability as:

> "The ease with which a software system or component can be modified to correct faults, improve performance or other attributes, or adapt to a changed environment."

The maintainability of software depends on quite a few factors. However, in general it must be easy to understand the software (how it works, what it does, and why it does it a particular way), easy to find what needs to change to achieve a given aim, easy to make those changes, and easy to check that the changes have not introduced any bugs. Writing readable code, as covered previously in this section, goes a long way to making code maintainable.

### Long- or Short-Lived Code?

You may be developing open-source software with the intent that it will live on after your project completes. It could be important to you that your software is adopted and used by other projects as this may help you get future funding. It can make your software more attractive to potential users if they have the confidence that they can fix bugs that arise or add new features they need, if they can be assured that the evolution of the software is not dependant upon the lifetime of your project.

On the other hand, you might want to knock together some code to prove a concept or to perform a quick calculation and then just discard it. But can you be sure you'll never want to use it again? Maybe a few months from now you'll realise you need it after all, or you'll have a colleague say "I wish I had a..." and realise you've already made one. A small investment in the maintainability of your code makes it easier to pick it up after a break, and can provide you with an insurance policy should your disposable software turn out to be more useful than you originally thought.

### The Cost of Neglecting Maintainability

When resources are tight, it's easy to focus on the bare minimum needed to get the software to do what it's meant to do and leave less pressing tasks, such as documentation, testing, and refactoring, until the end of the project. The plan often is to complete these tasks when time permits, and time rarely permits!

You can save time, in the short term, by not commenting code, not refactoring to make it more readable, not addressing compiler warnings, leaving aside tests, skipping documentation and not recording why something was implemented in a specific way. These actions all incur **technical debt**:

> *"Technical debt is the cost of additional rework caused by choosing an easy (limited) solution now instead of using a better approach that would take longer.”*

And - just like financial debt - it's a debt that gathers interest over time. Technical debt is paid off in the cost of maintenance. Software that is written without maintainability in mind requires a lot more effort to maintain than it did to develop. For this reason, many applications are replaced simply because the overhead to modify them becomes prohibitive.

Help is at hand! Developing maintainable software helps reduce technical debt. By thinking ahead and investing now you reduce the impact of changes in the future.

### How to Develop Maintainable Software

Developing maintainable software is like picnicking: once you're finished, leave your spot as you would like to find it yourself, or leave it in a better state than you found it. There are a number of principles, approaches and techniques that can help you develop maintainable software, and many of these are generally applicable to writing good software:

- *Start as you mean to go on:* write maintainable code from the outset, and make maintainability a key goal
- *Keep it functional:* write code in short, iterative cycles that aim to keep code in a working state
- *Refactor your code:* once your code gets messy and hard to understand, rewrite it to function the same but be easier to read
- *Get it reviewed:* Get others to look at your code to check it is understandable - particularly sections that are critically important
- *Document your code:* so you and others can understand it now and later
- *Use version control:* version control helps keep code and documentation up to date and synchronised, and allows you to roll back any parts of your code to previous versions if you run into trouble
- *Select sustainable technologies:* to avoid using libraries and other dependencies that may become outdated or even non-functional during development or use, be sure to choose technologies that have a good track record of delivering quality releases, and a sustainable, active development community.

### A Maintainability Checklist

Answering the following questions will help you judge the maintainability of your software:

- Can I find the code that is related to a specific problem or change?
- Can I understand the code? Can I explain the rationale behind it to someone else?
- Is it easy to change the code? Is it easy for me to determine what I need to change as a consequence? Are the number and magnitude of such knock-on changes small?
- Can I quickly verify a change (preferably in isolation)?
- Can I make a change with only a low risk of breaking existing features?
- If I do break something, is it quick and easy to detect and diagnose the problem? 

Now ask the questions again but, this time, adopt the perspective of someone else in your team and someone who is completely new to your software.


{% include links.md %}
