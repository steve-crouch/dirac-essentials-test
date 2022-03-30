---
title: "Documenting Code"
slug: dirac-test-document-review-documenting-code
teaching: 0
exercises: 0
questions:
- "How should we document and license our code?"
objectives:
- "Explain why documentation is important"
- "Describe the minimum components of software documentation to aid reuse"
- "Create a repository README file to guide others to successfully reuse a program"
- "Understand other documentation components and where they are useful"
- "Describe the basic types of open source software licence"
keypoints:
- "A huge contributor to the ability to reuse any software is documentation."
- "Having only a short documentation document that covers the basics for getting the software up and running goes a long way, and can be amended and added to later."
- "Documentation helps make your code reproducible."
- "By default, software code released without a licence conveys no rights for reuse."
- "Open source licences fall into two key categories: *copyleft* and *permissive*."
---

In previous episodes we've looked at what tools and techniques can help us design and develop good software for research. In this lesson we'll be looking at how we can document our software to ease reusability for others - including future versions of ourselves.


## Documenting Code to Improve Reusability

Reproducibility is a cornerstone of science, and scientists who work in many disciplines are expected to document the processes by which they've conducted their research so it can be reproduced by others. In medicinal, pharmacological, and similar research fields for example, researchers use logbooks which are then used to write up protocols and methods for publication.

Many things we've covered so far contribute directly to making our software reproducible - and indeed reusable - by others. A key part of this we'll cover now is software documentation, which is ironically very often given short shrift in academia. This is often the case even in fields where the documentation and publication of research method is otherwise taken very seriously.

A few reasons for this are that writing documentation is often considered:

- A low priority compared to actual research (if it's even considered at all)
- Expensive in terms of effort, with little reward
- Writing documentation is boring!

A very useful form of documentation for understanding our code is code commenting, and is most effective when used to explain complex interfaces or behaviour, or the reasoning behind why something is coded a certain way. But code comments only go so far.

Whilst it's certainly arguable that writing documentation isn't as exciting as writing code, it doesn't have to be expensive and brings many benefits. In addition to enabling general reproducibility by others, documentation...

- Helps bring new staff researchers and developers up to speed quickly with using the software
- Functions as a great aid to research collaborations involving software, where those from other teams need to use it
- When well written, can act as a basis for detailing algorithms and other mechanisms in research papers, such that the software's functionality can be *replicated* and re-implemented elsewhere
- Provides a descriptive link back to the science that underlies it. As a reference, it makes it far easier to know how to update the software as the scientific theory changes (and potentially vice versa)
- Importantly, it can enable others to understand the software sufficiently to *modify and reuse* it to do different things

In the next section we'll see that writing a sensible minimum set of documentation in a single document doesn't have to be expensive, and can greatly aid reproducibility.

> ## What Makes Good Documentation?
>
> Consider software you've used or developed in the past, where you've needed to refer to documentation. Which pieces of software had good documentation, and what made it good?
{: .challenge}


### Writing a README

A code's README file, the very first piece of documentation people see when visiting a GitHub code repository for example, is the first piece of documentation (perhaps other than publications that refer to it) that people should read to acquaint themselves with the software. It concisely explains what the software is about and what it's for, and covers the steps necessary to obtain and install the software and use it to accomplish basic tasks. Think of it not as a comprehensive reference of all functionality, but more a short tutorial with links to further information - hence it should contain brief explanations and be focused on instructional steps to get people started.

> ## How to Create a GitHub Repository README file?
> 
> If you're looking to write your own README for a GitHub repository, create a `README.md` file in the root directory of your repository. The `.md` indicates this is a **markdown** file, a lightweight markup language which is basically a text file with some extra syntax to provide ways of formatting them. A big advantage of them is that they can be read as plain-text files or as source files for rendering them with formatting structures, and are very quick to write. GitHub provides a very useful [guide to writing markdown](https://guides.github.com/features/mastering-markdown/) for its repositories.
{: .callout}

As an example, let's consider a README file for our clinical trial system we looked at in earlier lessons, written in GitHub markdown.

~~~
# Inflam
~~~
{: .language-bash}

So here, we're giving our software a name. Ideally something unique, short, snappy, and perhaps to some degree an indicator of what it does. We would ideally rename the repository to reflect the new name, but let's leave that for now. In markdown, the `#` designates a heading, two `##` are used for a subheading, and so on. The Software Sustainability Institute [guide on naming projects](https://software.ac.uk/resources/guides/choosing-project-and-product-names) and products provides some helpful pointers.

We should also add a short description.

~~~
Inflam is a data management system written in Python that manages trial data used in clinical inflammation studies.
~~~
{: .language-bash}

To give readers an idea of the software's capabilities, let's add some key features next:

~~~
## Main features

Here are some key features of Inflam:

- Provide basic statistical analyses over clinical trial data
- Ability to work on trial data in Comma-Separated Value (CSV) format
- Generate plots of trial data
- Analytical functions and views can be easily extended based on its Model-View-Controller architecture
~~~
{: .language-bash}

As well as knowing what the software aims to do and its key features, it's very important to specify what other software and related dependencies are needed to use the software (typically called `dependencies` or `prerequisites`):

~~~
## Prerequisites

Inflam requires the following Python packages:

- [NumPy](https://www.numpy.org/) - makes use of NumPy's statistical functions
- [Matplotlib](https://matplotlib.org/stable/index.html) - uses Matplotlib to generate statistical plots

The following optional packages are required to run Inflam's unit tests:

- [pytest](https://docs.pytest.org/en/stable/) - Inflam's unit tests are written using pytest
- [pytest-cov](https://pypi.org/project/pytest-cov/) - Adds test coverage stats to unit testing
~~~
{: .language-bash}

Here we're making use of markdown links, with some text describing the link within `[]` followed by the link itself within `()`.

That's got us started, but there are other aspects we should also cover:

- *Installation/deployment:* step-by-step instructions for setting up the software so it can be used
- *Basic usage:* step-by-step instructions that cover using the software to accomplish basic tasks
- *Contributing:* for those wishing to contribute to the software's development, this is an opportunity to detail what kinds of contribution are sought and how to get involved
- *Contact information/getting help:* which may include things like key author email addresses, and links to mailing lists and other resources
- *Credits/Acknowledgements:* where appropriate, be sure to credit those who have helped in the software's development or inspired it
- *Citation:* particularly for academic software, it's a very good idea to specify a reference to an appropriate academic publication so other academics can cite use of the software in their own publications and media. You can do this within a separate [CITATION text file](https://github.com/citation-file-format/citation-file-format) within the repository's root directory and link to it from the markdown
- *Licence:* a short description of and link to the software's licence

For more verbose sections, there are usually just highlights in the README with links to further information, which may be held within other markdown files within the repository or elsewhere.

We'll finish these off later. See [Matias Singer's curated list of awesome READMEs](https://github.com/matiassingers/awesome-readme) for inspiration.

### Other Documentation

There are many different types of other documentation you should also consider writing and making available that's beyond the scope of this course. The key is to consider which audiences you need to write for, e.g. end users, developers, maintainers, etc., and what they need from the documentation. There's a Software Sustainability Institute [blog post on best practices for research software documentation](https://www.software.ac.uk/blog/2019-06-21-what-are-best-practices-research-software-documentation) that helpfully covers the kinds of documentation to consider and other effective ways to convey the same information.

One that you should always consider is **technical documentation**. This typically aims to help other developers understand your code sufficiently well to make their own changes to it, which could include other members in your team (and as we said before, also a future version of yourself). This may include documentation that covers:

- **Software's architecture/design**, including the different components and how they fit together and database design (if a database is used)
- **API (Application Programmer Interface) documentation** that describes the interface points designed into your software for developers to use, e.g. for a software library
- **Technical tutorials or 'how tos'** to accomplish developer-oriented tasks, such as compiling or building the code, development environments, or how to extend or modify the code in particular ways

Of course, this all takes effort, and good and correct documentation requires that it is updated to keep in line with changes in the software which takes further effort. What's important is to consider what is *needed* and most helpful to other users and developers of the code: what problems will they (or do they) typically face when using the software? What needs explanation? What types of documentation should be written first?

> ## Improving Documentation
>
> Thinking again about software you've used or developed in the past, how could its usability have improved by additional documentation or changes to the existing documentation? What changes would you make?
{: .challenge}

## Choosing an Open Source Licence

Software licensing can be a whole course in itself, so we’ll just summarise here. Your institution’s Intellectual Property (IP) team will be able to offer specific guidance that fits the way your institution thinks about software.

In IP law, software is considered a creative work of literature, so any code you write automatically has copyright protection applied. This copyright will usually belong to the institution that employs you, but this may be different for PhD students. If you need to check, this should be included in your employment / studentship contract or talk to your university’s team that deals with intellectual property.

Since software is automatically under copyright, without a licence no one may:

- Copy it
- Distribute it
- Modify it
- Extend it
- Use it (actually unclear at present - this has not been properly tested in court yet)

Fundamentally there are two kinds of licence, **Open Source licences** and **Proprietary licences**, which serve slightly different purposes:

- *Proprietary licences* are designed to pass on limited rights to end users, and are most suitable if you want to commercialise your software. They tend to be customised to suit the requirements of the software and the institution to which it belongs - again your institutions IP team will be able to help here.
- *Open Source licences* are designed more to protect the rights of end users - they specifically grant permission to make modifications and redistribute the software to others. The website Choose A License provides recommendations and a simple summary of some of the most common open source licences.

Within the open source licences, there are two categories, **copyleft** and **permissive**:

- The permissive licences such as MIT and the multiple variants of the BSD licence are designed to give maximum freedom to the end users of software. These licences allow the end user to do almost anything with the source code.
- The copyleft licences such as the GNU General Public License (GPL) still give a lot of freedom to the end users, but any code that they write based on GPLed code must also be licensed under the same licence. This gives the developer assurance that anyone building on their code is also contributing back to the community. It’s actually a little more complicated than this, and the variants all have slightly different conditions and applicability, but this is the core of the licence.

Which of these types of licence you prefer is up to you and those you develop code with. If you want more information, or help choosing a licence, the [Choose An Open-Source Licence](https://choosealicense.com/) or [tl;dr Legal](https://tldrlegal.com/) sites can help.

> ## What if software doesn't have a licence?
> 
> It's a common misconception, but if a piece of software does not have a licence, it generally means others have no permissions from the software's creators to use, modify, or share the software. Simply that the code is freely and openly available is not enough - [without a license](https://choosealicense.com/no-permission/), the software is not (in a legal sense) usable by others.
{: .callout}

## What is a Version Number Anyway?

Software version numbers are everywhere, and there are many different ways to do it. A popular one to consider is [**Semantic Versioning**](https://semver.org/), where a given version number uses the format MAJOR.MINOR.PATCH. You increment the:

- MAJOR version when you make incompatible API changes
- MINOR version when you add functionality in a backwards compatible manner
- PATCH version when you make backwards compatible bug fixes

You can also add a hyphen followed by characters to denote a pre-release version, e.g. 1.0.0-alpha1 (first alpha release) or 1.2.3-beta4 (first beta release).


{% include links.md %}
