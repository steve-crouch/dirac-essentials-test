---
title: "Software Development Lifecycle"
slug: dirac-software-engineering-software-development-lifecycle
teaching: 0
exercises: 0
questions:
- "What is a software development process?"
- "Why is a development process important?"
- "What are the different development stages?"
objectives:
- "Explain some of the common issues found in academic software development"
- "Summarise the benefits of following a process of developing software"
- "Define the fundamental stages in software development"
- "Express how different process stages are connected"
- "Summarise the differences between the waterfall and agile models of software development"
keypoints:
- "Software engineering takes a wider view of software development beyond programming (or coding)."
- "Software you produce has inherent value."
- "Always assume your code will be read and used by others (including a future version of yourself)."
- "Additionally, aim to make your software reusable by others."
- "Reproducibility is a cornerstone of science, so ensure your software-generated results are reproducible."
- "Following a process makes development predictable, can save time, and helps ensure each stage of development is given sufficient consideration before proceeding to the next."
- "Ensuring requirements are sufficiently captured is critical to the success of any project."
---

In this section, we will take a look at coding - or writing software - as a *process of development*.

Even if you are now solely a software user and do not plan to develop any code, it's still useful to know how software is typically developed and what practices are used. You may find a good reason to get into developing code (even small, simple programs can be immensely useful), end up supervising others who will need to develop software, or become involved in projects where software is being developed: software, and its development, is becoming increasingly prevalent as a key tool for research across many fields of research.

> *"If you fail to plan, you are planning to fail."* - Benjamin Franklin

## Typical Software Development in Academia

Traditionally in academia, software - and the process of writing it - is often seen as a necessary but throwaway artefact in research. For example, there may be research questions (for a given research project), code is created to answer those questions, the code is run over some data and analysed, and finally a publication is written based on those results. These steps are often taken informally.

The terms *programming* (or even *coding*) and *software engineering* are often used interchangeably. They are not. Programmers or coders tend to focus on one part of the software development process: implementation, more than any other. In academic research, often they are writing software for themselves - they are their own stakeholders. And ideally, they are writing software from a design, that fulfils a research goal to publish research papers.

Someone who is engineering software, on the other hand takes a wider view:

- The *lifecycle* of software: from understanding what is needed, to writing the software and using/releasing it, to what happens afterwards.
- Who will (or may) be involved: software is written for *stakeholders*. This may only be the researcher initially, but there is an understanding that others may become involved later (even if that isn't evident yet). A good rule of thumb is to always assume that code will be read and used by others later on, which includes yourself!
- Software (or code) is an asset: software inherently contains value - for example, in terms of what it can do, the lessons learned throughout its development, and as an implementation of a research approach (i.e. a particular research algorithm, process, or technical approach).
- As an asset, it could be reused: again, it may not be evident initially that the software will have use beyond it's initial purpose or project, but there is an assumption that the software - or even just a part of it - could be reused in the future.


### The Levels of Software Reusability

We mentioned that having reusable software is a good idea, so let’s take a closer look at what we mean by that.

Firstly, whilst we want to ensure our software is reusable by others, as well as ourselves, we should be clear what we mean by ‘reusable’. There are a number of definitions out there, but a helpful one written by [Benureau and Rougler in 2017](https://dx.doi.org/10.3389/fninf.2017.00069) offers the following levels by which software can be characterised:

1. Re-runnable: the code is simply executable and can be run again (but there are no guarantees beyond that)
2. Repeatable: the software will produce the same result more than once
3. Reproducible: published research results generated from the same version of the software can be generated again from the same input data
4. Reusable: easy to use, understand, and modify
5. Replicable: the software can act as an available reference for any ambiguity in the algorithmic descriptions made in the published article. That is, a new implementation can be created from the descriptions in the article that provide the same results as the original implementation, and that the original - or reference - implementation, can be used to clarify any ambiguity in those descriptions for the purposes of reimplementation

Later levels imply the earlier ones. So what should we aim for? As researchers who develop software - or developers who write research software - we should be aiming for at least the fourth one: reusability. Reproducibility is required if we are to successfully claim that what we are doing when we write software fits within acceptable scientific practice, but it is also crucial that we can write software that can be *understood* by others. Where ‘others’, of course, can include a future version of ourselves: coming back and understanding our own code even after only six months can be difficult!

> ## What Do You Think?
> 
> Have you used any academically-produced software in your work, or perhaps developed some yourself? What was good about it, what were its shortcomings, and what aspects do you think should have been given greater attention during its development (or even afterwards)?
{: .challenge}

## The Software Development Process

The typical stages of a software development process can be categorised as follows:

- **Requirements gathering:** the process of identifying and recording the exact requirements for a software project before it begins. This helps maintain a clear direction throughout development, and sets clear targets for what the software needs to do.
- **Design:** where the requirements are translated into an overall design for the software. It covers what will be the basic software 'components' and how they'll fit together, as well as the tools and technologies that will be used, which will together address the requirements identified in the first stage.
- **Implementation:** the software is developed according to the design, implementing the solution that meets the requirements set out in the requirements gathering stage.
- **Testing:** the software is tested with the intent to discover and rectify any defects, and also to ensure that the software meets its defined requirements, i.e. does it actually do what it should do reliably?
- **Deployment:** where the software is deployed and used for its intended purpose.
- **Maintenance:** where updates are made to the software to ensure it remains fit for purpose, which typically involves fixing any further discovered issues and evolving it to meet new or changing requirements.

Whether you are aware of them or not, these stages are followed implicitly or explicitly in every software project. What is required is always considered, for example, even if it isn't explored sufficiently or well understood.

Following a process of development offers some major benefits:

- **Stage gating:** a quality *gate* at the end of each stage, where stakeholders review the stage's outcomes to decide if that stage has completed successfully before proceeding to the next one (and even if the next stage is warranted at all - for example, it may be discovered during requirements of design that development of the software isn't practical or even required)
- **Predictability:** each stage is given attention in a logical sequence; the next stage should not begin until prior stages have completed. Returning to a prior stage is possible and may be needed, but may prove expensive, particularly if an implementation has already been attempted. However, at least this is an explicit and planned action.
- **Transparency:** essentially, each stage generates output(s) into subsequent stages, which presents opportunities for them to be published as part of an open development process.
- **It saves time:** a well-known result from [empirical software engineering studies](https://web.archive.org/web/20160731150816/http://superwebdeveloper.com/2009/11/25/the-incredible-rate-of-diminishing-returns-of-fixing-software-bugs/) is that it becomes exponentially more expensive to fix mistakes in future stages. For example, if a mistake takes 1 hour to fix in requirements, it may take 5 times that during design, and perhaps as much as 20 times that to fix if discovered during testing.

> ## How Should it Have Been Improved?
>
> For your software example used in the first exercise (or perhaps another piece of software entirely), for each problem you identified, within which stage do you think that aspect should have been addressed?
{: .challenge}

FIXME: briefly show alternative arrangements of how the process can work, e.g. agile?


## The Importance of Getting Requirements Right

The importance of gaining a solid understanding for what is required for a software project (or any project) before you begin cannot be overstated. As mentioned, going back and changing an existing implementation is an expensive process.

Requirements can be categorised in many ways, but at a high level a useful way to split them is into *Business Requirements*, *User Requirements*, and *Solution Requirements*. Let's take a look at these now. As an exemplar we'll use some hypothetical statistical analysis software for clinical trials to illustrate the differences between them.

FIXME: change example to an HPC-oriented research project: from a simple software package, to running it on DiRAC, to results analysis for publication

### Business Requirements

Business requirements describe what is needed from the perspective of the organisation, and define the strategic path of the project, e.g. to increase profit margin or market share, or embark on a new research area or collaborative partnership. These are captured in something like a Business Requirements document.

For adapting our clinical trial software project, example business requirements could include:

- BR1: ensure statistical quality of clinical trial reporting meets the needs of external audits
- BR2: throughput of trial analyses is able to meet high demand during peak periods

### User (or Stakeholder) Requirements

These define what particular stakeholder groups each expect from an eventual solution, essentially acting as a bridge between the higher-level business requirements and specific solution requirements. These are typically captured in a User Requirements Specification.

For our software, they could include things for trial managers such as (building on the business requirements):

- UR1 (from BR1): support for statistical measures in generated trial reports as required by revised auditing standards (standard deviation, ...)
- UR2 (from BR2): support for producing textual representations of statistics in trial reports as required by revised auditing standards
- UR3 (from BR2): ability to have an individual trial report processed and generated in under 30 seconds

### Solution Requirements

Solution (or product) requirements describe characteristics that a concrete solution or product must have to satisfy the stakeholder requirements. They fall into two key categories:

- *Functional Requirements* focus on functions and features of a solution. For our software, building on our user requirements, e.g.
  - SR1 (from UR1): statistical measures include mean average, minimum, maximum, and standard deviation
  - SR2 (from UR2): generate a textual representation of statistics that can be imported into auditing documents
- *Non-functional Requirements* focus on *how* the behaviour of a solution is expressed or constrained, e.g. performance, security, usability, or portability. These are also known as *quality of service* requirements. For our project, e.g.:
  - SR3 (from UR3): generate graphical statistics report on clinical workstation configuration in under 30 seconds

### From Requirements to Implementation

In practice, these different types of requirements are sometimes confused and conflated when different classes of stakeholder are discussing them, which is understandable: each group of stakeholder has a different view of *what is required* from a project. The key is to understand the stakeholder's perspective as to how their requirements should be classified and interpreted, and for that to be made explicit. A related misconception is that each of these types are simply requirements specified at different levels of detail. At each level, not only are the perspectives different, but so are the nature of the objectives and the language used to describe them.


{% include links.md %}
