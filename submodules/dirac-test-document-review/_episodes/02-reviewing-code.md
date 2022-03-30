---
title: "Reviewing Code"
slug: dirac-test-document-review-reviewing-code
teaching: 0
exercises: 0
questions:
- "How can others help me improve my code?"
- ""
objectives:
- "List the benefits of code reviews."
- "Explain what happens in a code review."
- "Describe some approaches to help run an effective code review."
keypoints:
- "Code review is where at least one other person looks at parts of a codebase in order to improve its code readability, understandability, quality and maintainability."
- "The first hour of code review matters the most."
---

So far in this course we’ve focused on learning software design and (some) technical practices, tools and infrastructure that help the development of software. We've also looked at developing tests to check our code which is one way to reassure ourselves and others that our code behaves as intended. But what about the perspectives of other people, such as others in our lab group or development team, and importantly, how about any key collaborators or end users of our software?

In this episode we'll look at the benefits of review - by others in our team looking at our code from a developer's perspective, and (at a higher level) by key stakeholders reviewing the software from an end-user's perspective.


## Code Review

As we've already mentioned, a good rule of thumb is to assume that others - including a future version of yourself - will **look** at our code. Code review brings that process forward, by having members of our team, lab, or other collaborators, review parts of our code and provide feedback. Note that we didn't mention reviewing *all* the code: code reviews are most effective and efficient when they focus on the most important parts that are critical to the software's functions.

### What are the Benefits of Code Review?

An effective code review:

- Prevents errors from creeping into your software by improving code quality at an early stage of the software development process
- Provides developers with feedback from more senior developers to improve their own coding practices and expertise
- Helps with learning, i.e. sharing knowledge about the codebase, solution approaches, expectations regarding quality, coding standards, etc.
- Helps increase the sense of collective code ownership and responsibility of code, which in turn helps increase the “bus factor” and reduce the risk or having a single person “responsible” for a certain part of the codebase

According to Michael Fagan, the author of the code inspection technique, rigorous inspections can remove 60-90% of errors from the code even before the first tests are run ([Fagan, 1976](https://doi.org/10.1147%2Fsj.153.0182)).

### How to do a Code Review?

There are many ways to accomplish an effective code review. It could be in an informal meeting between two people at a desk, with the code writer leading another through a portion of code, explaining its intent and the rationale for decisions made within the implementation, or it could be done within a larger setting, with the same goals but perhaps with a few colleagues or developers and the code writer presenting from a projector.

Here are some things to consider to get the most out of a code review (see blogs from [Swarmia](https://www.swarmia.com/blog/a-complete-guide-to-code-reviews/) and [Smartbear](https://smartbear.com/learn/code-review/best-practices-for-peer-code-review/) for more details):

1. **Decide the focus of a code review:** are you reviewing overall code design, a module's code or tests, a set of key changes across a codebase, or considering a particular code issue and how to solve it?
2. **Do not review for too long in one sitting:** according to [Best Kept Secrets of Peer Code Review (Cohen, 2006)](https://www.amazon.co.uk/Best-Kept-Secrets-Peer-Review/dp/1599160676), the first hour of review matters the most as detection of defects significantly drops after this period. [Studies into code review](https://smartbear.com/resources/ebooks/the-state-of-code-review-2020-report/) also show that you should not review more than 400 lines of code at a time. Conducting more frequent shorter reviews seems to be more effective.
3. **Focus on important parts of the code:** to be efficient, reserve code review for critical portions of code.
4. **Communicate clearly and effectively:** when reviewing code, be explicit about the action you request from the author.
5. **Foster a positive feedback culture:** ensure give feedback about the code, not about the author, and accept that there are multiple correct solutions to a problem. Sandwich criticism with positive comments and praise to keep the review positive.

> ## Tool-assisted Code Review
> 
> Another way to accomplish code reviews is via a **tool-assisted code review**. Instead of undertaking a code review with others physically present, a tool is used to facilitate the process of code review. These tools can help by displaying what code files have changed and require review, and facilitating a conversation between team members (in the role of developer and reviewer). GitHub, for example, has a **pull request** feature on its code repositories, an increasingly popular method of delegating the task of review to others. The name pull request suggests you are requesting that your changes are accepted into the repository.
> 
> With a pull request, changes are made to a source code repository in the form of commits that are then submitted as a pull request to the repository. These pull requests highlight the code changes from the commits and can be delegated to and reviewed by others, who have an opportunity to insert comments on the changes into their review. Once any reviews are submitted, a decision can then be made as to whether these changes can be integrated into the code base or rejected, at which point the pull request has served its purpose.
{: .callout}

> ## Action Stations!
>
> Take a look at the GitHub code repository at <https://github.com/softwaresaved/rf4>. Examine the contents of the repository (code, documentation, other assets) and consider what you think needs to be improved in order for you to use it successfully. What would make it difficult to install and use? What would be the top two things you would address first and why?
{: .challenge}

## Acceptance Testing

Another aspect we've already mentioned is that we should assume that others - including a future version of yourself - will **run** (essentially, use) our code.

FIXME: add content for acceptance testing


{% include links.md %}
