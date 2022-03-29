---
layout: workshop      # DON'T CHANGE THIS.
---

<h2 id="general">General Information</h2>
<p id="overview-general">
The DiRAC Essentials Level Training is a basic introduction to the principles of HPC and the tools needed to work on an HPC system. Once you have completed the course you will be able to do more science of higher impact (and we hope you will have more fun as well!). And if we have a well-trained cohort we can invest in much more powerful equipment that is much closer to the bleeding edge and so allow you to generate the new high impact results that will let you and your group to be seen as leaders in your field.

It will also make you much more employable. Real programming and IT skills are making a big comeback both in Academia and Industry. We need to equip you with these skills to improve your career progression. In short, we are trying to create a virtuous circle that will benefit both you, your science and your group’s scientific reputation.
</p>

<p id="overview-aims">
  <strong>Course Aims:</strong>

  Introduce the student to Unix environment and its computing tools, including file management systems and editors.                           	                                                                       
</p>

<ul>
  <li>Introduce basic scripting ideas</li>
  <li>Introduce version control</li>
  <li>Introduce the basics of good software engineering practise</li>
  <li>Introduce the principles of code scaling</li>
  <li>Introduce good networking practise</li>
  <li>Provide the opportunity to develop independent learning skills</li>
</ul>

<p id="overview-outcomes">
  <strong>Learning Outcomes:</strong>
  The learner will be able to:
</p>

<ul>
  <li>Use the tools of the Unix environment, file management, and common editors</li>
  <li>Implement a command script</li>
  <li>Use version control tools</li>
  <li>Understand the principles of software design</li>
  <li>Understand the principles of software testing</li>
  <li>Describe the principles of code scaling</li>
  <li>Use tools to demonstrate good networking practise</li>
</ul>

{% if site.venue == "TBC" %}
<p>
  <strong> Workshop location TBC </strong>
</p>
{% elsif site.venue == "online" %}
<p id="where">
  Online at <a href="{{site.address}}">{{site.platform-name}}</a>.
  If you need a password or other information to access the training,
  the instructor will pass it on to you before the workshop.
</p>
{% elsif site.kind != "course" %}
<p id="where">
  <strong>Where:{{site.venue}}</strong>
  <strong>Address:{{site.address}}</strong>
</p>
{% endif %}


{% comment %}
DATE

This block displays the date.
{% endcomment %}
{% if site.humandate %}
<p id="when">
  <strong>When:</strong>
  {{site.humandate}}.
</p>
{% endif %}

{% comment %}
SPECIAL REQUIREMENTS

Modify the block below if there are any special requirements.
{% endcomment %}
<p id="requirements">
  <strong>Requirements:</strong>
  {% if online == "false" %}
    Participants must bring a laptop with a
    Mac, Linux, or Windows operating system (not a tablet, Chromebook, etc.) that they have administrative privileges on.
  {% else %}
    Participants must have access to a computer with a
    Mac, Linux, or Windows operating system (not a tablet, Chromebook, etc.) that they have administrative privileges on, and
    have successfully completed the DiRAC account registration process with an SSH key able to access DiRAC resources.
  {% endif %}
  They should have a few specific software packages installed (listed <a href="#setup">below</a>).
</p>

{% comment %}
ACCESSIBILITY

Modify the block below if there are any barriers to accessibility or
special instructions.
{% endcomment %}
<p id="accessibility">
  <strong>Accessibility</strong>
{% if online == "false" %}
  We are committed to making this workshop
  accessible to everybody.  For workshops at a physical location, the workshop organizers have checked that:
</p>
<ul>
  <li>The room is wheelchair / scooter accessible.</li>
  <li>Accessible restrooms are available.</li>
</ul>
<p>
  Materials will be provided in advance of the workshop and
  large-print handouts are available if needed by notifying the
  organizers in advance.  If we can help making learning easier for
  you (e.g. sign-language interpreters, lactation facilities) please
  get in touch (using contact details below) and we will
  attempt to provide them.
</p>
{% else %}
<p>
  We are dedicated to providing a positive and accessible learning environment for all. Please
  notify the instructors in advance of the workshop if you require any accommodations or if there is
  anything we can do to make this workshop more accessible to you.
</p>
{% endif %}

{% comment %}
CONTACT EMAIL ADDRESS

Display the contact email address set in the configuration file.
{% endcomment %}
<p id="contact">
  <strong>Contact:</strong>
  Please email
  {% if site.email %}
  {% for email in site.email %}
  {% if forloop.last and site.email.size > 1 %}
  or
  {% else %}
  {% unless forloop.first %}
  ,
  {% endunless %}
  {% endif %}
  <a href='mailto:{{email}}'>{{email}}</a>
  {% endfor %}
  {% else %}
  to-be-announced
  {% endif %}
  for more information.
</p>


<hr/>

<!--
{% comment %}
CODE OF CONDUCT
{% endcomment %}
<h2 id="code-of-conduct">Code of Conduct</h2>

<p>
Everyone who participates in Carpentries activities is required to conform to the <a href="https://docs.carpentries.org/topic_folders/policies/code-of-conduct.html">Code of Conduct</a>. This document also outlines how to report an incident if needed.
</p>

<p class="text-center">
  <a href="https://goo.gl/forms/KoUfO53Za3apOuOK2">
    <button type="button" class="btn btn-info">Report a Code of Conduct Incident</button>
  </a>
</p>
<hr/>
-->

<!--
{% comment %}
SURVEYS - DO NOT EDIT SURVEY LINKS
{% endcomment %}
<h2 id="surveys">Surveys</h2>
<p>Please be sure to complete these surveys before and after the workshop.</p>
<p><a href="{{ site.pre_survey }}{{ site.github.project_title }}">Pre-workshop Survey</a></p>
<p><a href="{{ site.post_survey }}{{ site.github.project_title }}">Post-workshop Survey</a></p>
<hr/>
-->

{% comment %}
SCHEDULE
This schedule is either used from swc or it is autogenerated by the rsg/schedule
and pulled from the lessons individually
{% endcomment %}

<h2 id="schedule">Course Syllabus</h2>

{% if site.carpentry == "swc" %}
{% include swc/schedule.html %}
{% elsif site.carpentry == "rsg" %}
{% include rsg/schedule.html %}
{% endif %}

<hr/>

<h2 id="setup">Setup</h2>

<p>
  To participate in
  {% if site.kind == "course" %}
  this online self-learning
  {% elsif site.carpentry == "swc" %}
  a Software Carpentry workshop
  {% elsif site.carpentry == "rsg" %}
  this training workshop
  {% endif %}
  you will need access to software as described below.
  In addition, you will need an up-to-date web browser.
</p>
<p>
  We maintain a list of common issues that occur during installation as a reference for instructors
  that may be useful on the
  <a href = "{{site.swc_github}}/workshop-template/wiki/Configuration-Problems-and-Solutions">Configuration Problems and Solutions wiki page</a>.
</p>

{% comment %}
These are the installation instructions for the tools used
during the workshop.
If using RSG these are generated from each individual lesson
{% endcomment %}

{% if site.carpentry == "swc" %}
{% include swc/setup.html %}
{% elsif site.carpentry == "rsg" %}
The instructions for all the software can be found <a href = "./setup"> on the setup page.</a>
{% endif %}
