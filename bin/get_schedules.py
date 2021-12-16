"""Create schedule for the workshop.

Determines which lesson schedules are required by reading _config.yml. The
schedule for each lesson is modified by a delta time to account for different
start times to what is in the schedule. The schedules are written then in an
(n x 2) array. This script updates _includes/rsg/schedule.html.
"""

import datetime
import yaml
import pandas
import textwrap
from bs4 import BeautifulSoup as bs


def get_yaml_config():
    """Open the YAML config file for the website.

    Returns
    -------
    config: dict
        The configuration for the website.
    """
    with open("_config.yml", "r") as fp:
        config = yaml.load(fp, yaml.Loader)

    return config


def get_time_object(time_string):
    """Convert a string into a datetime object.

    Parameters
    ----------
    time_string: str
        The time string to convert.

    Returns
    -------
    time_object: datetime.datetime
        The converted string as a datetime object.
    """
    if type(time_string) is str:
        try:
            time = datetime.datetime.strptime(time_string, "%I:%M %p")   # start-time: 9:30 am
        except ValueError:
            time = datetime.datetime.strptime(time_string, "%H:%M")      # start-time: "9:30"
    elif type(time_string) is int:
        hours, minutes = divmod(time_string, 60)
        time = datetime.datetime.strptime(f"{hours}:{minutes}", "%H:%M") # start-time: 9:30
    else:
        raise ValueError(f"start-time {time_string} is an invalid format: accept 24 hr (15:00) or 12 hr with am/pm (3:00 pm)")

    return time


def write_overall_schedule(schedules):
    """Write the new schedule to _includes/rsg/schedule.html.

    Parameters
    ----------
    html: str
        The HTML code of the schedule.
    """
    html = "<div class=\"row\">"
    html += schedules
    html += "</div>"

    with open("_includes/rsg/schedule.html", "w") as fp:
        fp.write(bs(html, "html.parser").prettify())


def write_detailed_lesson_schedule(lesson_name):
    """Create a detailed lesson schedule landing page for each lesson.

    The schedule is based on a modifed version of syllabus.html to work better
    work the workshop format.

    Parameters
    ----------
    lesson_name: str
        The name of the lesson.
    """
    schedule_markdown = textwrap.dedent(f"""---
    title: ""
    slug: {lesson_name}-schedule
    layout: page
    ---
    {{% include episode_navbar.html episode_navbar_title=true %}}
    <div align="center"><h1>Lesson Schedule</h1><br></div>
    {{% include syllabus.html  gh-name="{lesson_name}" %}}
    {{% include episode_navbar.html episode_navbar_tile=true %}}
    """)

    schedule = "\n".join([line.lstrip() for line in schedule_markdown.splitlines()])

    with open(f"collections/_episodes/{lesson_name}-lesson/00-schedule.md", "w") as fp:
        fp.write(schedule)


website_config = get_yaml_config()
html_schedules = ""  # HTML string containing the tables for each schedule

# Go through each lesson to get and update the schedule, depending on start time

for lesson in website_config["lessons"]:

    lesson_title = lesson.get("title", None)
    lesson_name = lesson.get("gh-name", None)
    lesson_date = lesson.get("date", None)              # can be a list
    lesson_start = lesson.get("start-time", None)  # can be a list

    if [thing for thing in (lesson_name, lesson_date, lesson_title, lesson_start) if thing is None]:
        raise ValueError(f"gh-name, date, title, and start-time are required for each lesson")

    # Since we allow multiple dates and start times per lesson, we need to be
    # able to iterate over even single values so turn into list

    if type(lesson_date) is not list:
        lesson_date = [lesson_date]
    if type(lesson_start) is not list:
        lesson_start = [lesson_start]

    # Get the schedule(s) for the lesson into a dataframe and also the html
    # so we can search for the permalinks

    with open(f"_includes/rsg/{lesson_name}-lesson/schedule.html", "r") as fp:
        schedule_html = fp.read()

    soup = bs(schedule_html, "html.parser")
    all_schedules = pandas.read_html(schedule_html, flavor="bs4")

    # Loop over each schedule table, if the lesson has multiple schedules

    for i, schedule in enumerate(all_schedules):

        schedule.columns = ["time", "session"]
        permalink = soup.find_all("a", href=True)[i]["href"]  # assume each table has a permalink to a lesson
        start_time = get_time_object(lesson_start[i])
        original_start = get_time_object(schedule["time"][0])
        date = lesson_date[i]

        # Calculate the time difference between the start time and the start
        # time in the original schedule. This delta time (in minutes) is added
        # to each time in the original schedule

        delta_minutes = divmod((start_time - original_start).total_seconds(), 60)[0]

        # Construct the schedule table for this lesson, adding delta_minutes to
        # each original entry, and add the schedule table to the html template

        if len(all_schedules) > 1:
            title = f"Day {i + 1}: {lesson_title}"
        else:
            title = lesson_title

        table = f"""
            <div class="col-md-6">
                <a href="{lesson_name}-schedule"><h3>{title}</h3></a>
                <h4>{date}</h4>
                <table class="table table-striped">
        """

        for time, session in zip(schedule["time"], schedule["session"]):
            actual_time = datetime.datetime.strptime(time, "%H:%M") + datetime.timedelta(minutes=delta_minutes)
            table += f"<tr> <td> {actual_time.hour:02d}:{actual_time.minute:02d} </td>    <td> {session} </td> </tr>\n"

        table += """
                </table>
            </div>
        """

        html_schedules += table

    write_detailed_lesson_schedule(lesson_name)

write_overall_schedule(html_schedules)
