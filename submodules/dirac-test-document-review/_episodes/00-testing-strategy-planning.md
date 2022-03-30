---
title: "Test Strategy, Planning, and Running Tests"
slug: dirac-test-document-review-test-strategy-planning
teaching: 0
exercises: 0
questions:
- "Does the code we develop work the way it should do?"
- "Can we (and others) verify these assertions for themselves?"
- "To what extent are we confident of the accuracy of results that appear in publications?"
objectives:
- "Explain the reasons why testing is important"
- "Explain the differences between a test plan and a test strategy"
- "List what's typically included within a test case"
- "Describe the benefits and drawbacks of manual and automated testing"
- "Describe how unit tests can verify the correct behaviour of a program's functions"
keypoints:
- "A test plan forms the foundation of any testing."
- "We should write tests to verify that functions generate expected output given a set of specific inputs."
- "The three main types of automated tests are **unit tests**, **functional tests** and **regression tests**."
- "We can use a unit testing framework like `pytest` to structure and simplify the writing of tests."
- "Testing program behaviour against both valid and invalid inputs is important and is known as **data validation**."
---

Being able to demonstrate that a process generates the right results is important in any field of research, whether it’s software generating those results or not. For the sake of argument, if each line we write has a 99% chance of being right, then a 70-line program will be wrong more than half the time. We need to do better than that, which means we need to test our software to catch these mistakes.


## What Is Software Testing?

So when writing software we need to ask ourselves some key questions:

- Does the code we develop work the way it should do?
- Can we (and others) verify these assertions for themselves?
- Perhaps most importantly, to what extent are we confident of the accuracy of results that appear in publications?

If we are unable to demonstrate that our software fulfills these criteria, why would anyone use it? Having a well-defined and regularly used test strategy, test plan and test cases can help give us and others confidence that our software works as expected.

### Test Strategy vs Test Plans

There are two key aspects to consider before we start thinking about actual tests:

- A **test plan** defines the scope of what exactly is to be tested for a given piece of software, the objectives for testing, which tools or techniques will be used, how the software will be checked, and who will be involved. A test plan applies to a specific piece of software.
- A **test strategy** contains guiding principles for testing, that covers the testing process e.g. how testing will be done, which formats to be used for defining test cases and recording results, and how tests will be reported. This may apply to many software projects, although in smaller groups and projects the test strategy may be defined within the test plan itself.

### The Test Case

The fundamental building block of testing itself is a *test case*, with test cases being run following the test plan. A project's test cases are typically derived from the project's specified requirements, so that if the software passes these tests it is said to fulfil those requirements.

Each test case covers the following information:

- A unique name or number to identify it
- The software feature(e) covered by the test case (specifying any specific requirements from which this feature is derived, e.g. SR1 or SR2)
- The input data to use for this test
- What needs to be done to ensure the software is in the correct state for the test
- How exactly to run the test with the input data
- The predicted result of running the test

When the test is run, the following are also noted (perhaps as an instance of the test plan, or within an issue on the code's source repository:

- Date the test is run
- A description of the actual result
- Whether or not the test was successful (i.e. the actual result are equal to the predicted result)
- Which (if any) errors were discovered

When followed, testing enables those within any software development effort to verify the software is behaving correctly. Software, particularly within academic research, is prone to the need for change during its development, so a successfully executed test plan and set of test cases provides assurance that the software's functionality continues to behave as intended despite these changes.

> ## Design Tests for a New Feature
> 
> Look back at the Solution Requirements (SR1 or SR2) covered in the [Principles of Software Engineering Lesson](https://southampton-rsg-training.github.io/dirac-essentials-test/dirac-software-engineering-software-development-lifecycle#the-importance-of-getting-requirements-right). Write a couple of test cases that verify that the feature behaves as specified in the requirements.
{: .challenge}


## Manual vs Automated Testing

We can and should extensively test our software manually, and it is a critical part of ensuring software functions correctly. It has the major benefit that the tester can observe the application during the actual test process, and interact with it as required to fulfill the test. As such, manual testing is also well-suited to testing aspects such as graphical user interfaces and reconciling visual outputs against inputs.

However, manual testing is often time consuming and prone to error. Another style of testing is automated testing, where we write code that tests the functions of our software. Since computers are very good and efficient at automating repetitive tasks, we should take advantage of this wherever possible.

On the other hand, automation enables us to define a potentially complex process in a repeatable way that is far less prone to error than manual approaches,and typically much faster. Once written, automated tests can be run many times, for instance whenever we change our code. And not just for ourselves: when others make use of your code, running these tests can help them build confidence in your code too.

Thus, once defined, automation can also save us a lot of effort, particularly in the long run. There are three main types of automated tests:

- **Unit tests** are tests for small and specific units of functionality, e.g. determining that a particular function returns output as expected given specific inputs.
- **Functional or integration tests** work at a higher level, and test functional paths through your code, e.g. given some specific inputs, a set of interconnected functions across a number of modules (or the entire code) produce the expected result. These are particularly useful for exposing faults in how functional units interact.
- **Regression testing** is kind of a special case of testing that makes sure that your program’s output and behaviour hasn’t changed. For example, after making changes to your code to add new functionality or fix a bug, you may re-run your unit or integration tests to make sure they haven't broken anything. You may also add a new specific regression test to highlight if a particular bug has returned.

A collection of automated tests is often referred to as a *test suite*.

> ## Testing: a Rule of Thumb
>
> Overall, a good guiding principle behind testing is to *fail fast*. By prioritising the identification of failure – where unit testing can really help us – affords us the opportunity to find and resolve issues early, in particular, before they may lead to published results.
{: .callout}

## Example: Unit Testing

Let's have a look at how we may structure test cases as unit tests, within a *unit testing framework*. In such a framework we define our tests we want to run as functions, and the framework automatically runs each of these functions in turn, summarising the outputs.

Most people don’t enjoy writing tests, so if we want them to actually do it, it must be easy to:

- Add or change tests
- Understand the tests that have already been written
- Run those tests, and
- Understand those tests’ results

Test results must also be reliable. If a testing tool says that code is working when it’s not or reports problems when there actually aren’t any, people will lose faith in it and stop using it.

Let's assume we have some code that computes the factorial of a given number, for example in Python:

~~~
def factorial(n):
    """
    Calculate the factorial of a given number.

    :param int n: The factorial to calculate
    :return: The resultant factorial
    """
    if n == 0 or n == 1:
        return 1
    else:
        return  n * factorial(n-1)
~~~
{: .language-python}

So, factorial(3) will give us 6, factorial(5) gives us 120. You'll notice we have also included a Python docstring at the head of the function, briefly describing what the function does, its input parameter, and what it returns, which is good practice.

Now let's see what some unit tests might look like using an example Python unit testing framework:

~~~
from mymath.factorial import factorial

def test_factorial_3():
    assert factorial(3) == 6

def test_factorial_5():
    assert factorial(5) == 120

def test_factorial_10():
    assert factorial(10) == 3628800
~~~
{: language-python}

Each of these test functions, in a general sense, is called a test case - these are a specification of:

- **Inputs**, e.g. the numbers we pass to our factorial function
- **Execution conditions** - what we need to do to set up the testing environment to run our test, e.g. in this case, we need to import the factorial function from our mymath source code. We could include this import statement within each test function, but since we are testing the same function in all of them, for brevity we'll include it at the top of the script.
- **Testing procedure**, e.g. call our factorial function with an input number and confirm that it equals our expected output. Here, we use Python's assert statement to do this, which will return false and fail the test if this condition does not hold
- **Expected outputs**, e.g. the numbers to which we compare the result of calling the factorial function

Note the very strong similarity between these aspects and the definition of test case we had earlier. And here, we’re defining each of these things for a test case we can run independently that requires no manual intervention.

Going back to our list of requirements, how easy is it to run these tests? Well, these tests are written to be used by a Python package called [pytest](https://docs.pytest.org/). Pytest is a testing framework that allows you to write test cases using Python.

> ## What About Unit Testing in Other Languages?
>
> Other unit testing frameworks exist for Python, including Nose2 and Unittest, and the approach to unit testing can be translated to other languages as well, e.g. FRUIT for Fortran, JUnit for Java (the original unit testing framework), Catch for C++, etc.
{: .callout}

Now we can run these tests using pytest:

~~~
$ python3 -m pytest

============================= test session starts ==============================
platform linux -- Python 3.8.10, pytest-6.2.5, py-1.10.0, pluggy-1.0.0
rootdir: /home/user
collected 3 items

tests/test_factorial.py ...                                              [100%]

============================== 3 passed in 0.02s ===============================
~~~
{: .language-bash}

So what's happening here? When started without any arguments, pytest does a number of things to look for tests you have written. By default, it will recursively check in directories (including the current one) for files that begin with test_ and end with .py, and if found, it looks for functions whose names also start with the letters test_ and runs each one. It will even find test methods matching the same pattern within classes beginning with Test. See the pytest documentation on good practices if you'd like to know more about how pytest finds tests, and other file layouts you can use to arrange your tests.

Notice the `...` after our test script:

- If the function completes without an assertion being triggered, we count the test as a success (indicated as .).
- If an assertion fails, or we encounter an error, we count the test as a failure (indicated as F). The error is included in the output so we can see what went wrong.

If we have many tests, we essentially get a report indicating which tests succeeded or failed.

> ## Why Should We Test Invalid Input Data?
>
> Testing the behaviour of inputs, both valid and invalid, is a really good idea and is known as *data validation*. Even if you are developing command line software that cannot be exploited by malicious data entry, testing behaviour against invalid inputs prevents generation of erroneous results that could lead to serious misinterpretation (as well as saving time and compute cycles which may be expensive for longer-running applications). It's generally best not to assume your user's inputs will always be rational.
{: .callout}


{% include links.md %}
