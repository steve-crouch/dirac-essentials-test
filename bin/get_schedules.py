"""Create schedule for the workshop.

Determines which lesson schedules are required by reading _config.yml. The
schedule for each lesson is modified by a delta time to account for different
start times to what is in the schedule. The schedules are written then in an
(n x 2) array. This script updates _includes/rsg/schedule.html.
"""

import datetime
import yaml
import pandas
import glob
import textwrap
from bs4 import BeautifulSoup as bs
from pathlib import Path
import string
from enum import Enum
import dateutil


class LessonType(Enum):
    """Enum for the different types of lessons.
    """
    markdown = "episode"
    r_markdown = "episode_r"


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


def get_date_object(datestr):
    """Convert a date string into a datetime object.

    On failure to convert a string, None is returned.

    Parameters
    ----------
    datestr: str
        The string of the date, in format YYYY-MM-DD.

    Returns
    -------
    date: datetime.date
        The date object. If unable to parse, then None is returned instead.
    """
    if datestr is None:
        return None

    if isinstance(datestr, datetime.date):
        return datestr
    elif not isinstance(datestr, str):
        raise ValueError(f"datestr is not a string but {type(datestr)}")

    try:
        date =  dateutil.parser.parse(datestr).date()
    except dateutil.parser.ParserError:
        date =  None

    return date


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


def write_detailed_lesson_schedule(lesson_name, start_time):
    """Create a detailed lesson schedule landing page for each lesson.

    The schedule is based on a modifed version of syllabus.html to work better
    with the workshop format. This function also renames the ordering of
    lessons, so the schedule will always be lesson 00.

    Parameters
    ----------
    lesson_name: str
        The name of the lesson.
    start_time: str
        The start time of the lesson.
    """
    containing_directory = f"collections/_episodes/{lesson_name}-lesson"
    for i, file in enumerate(sorted(glob.glob(f"{containing_directory}/[0-9]*.md"))):
        filepath = Path(file)
        new_file_name = f"{i + 1:02d}{filepath.stem.lstrip(string.digits)}.md"
        filepath.rename(f"{containing_directory}/{new_file_name}")

    schedule_markdown = textwrap.dedent(f"""---
    title: Lesson Schedule
    slug: {lesson_name}-schedule
    layout: schedule
    ---
    {{% include syllabus.html  name="{lesson_name}" start_time={start_time} %}}
    """)

    with open(f"{containing_directory}/00-schedule.md", "w") as fp:
        fp.write("\n".join([line.lstrip() for line in schedule_markdown.splitlines()]))


html_schedules = ""  # HTML string containing the tables for each schedule
website_config = get_yaml_config()

# Try to parse the start and end date for the workshop, to check that lessons
# are in the correct time frame. If the date is not a valid date, i.e. if it
# still says FIXME, then we do not check the start and end date.

workshop_start_date = get_date_object(website_config.get("startdate", None))
workshop_end_date = get_date_object(website_config.get("enddate", None))

# Iterate over each lesson, to add their schedule to the html_schedules string

for lesson in website_config["lessons"]:

    lesson_title = lesson.get("title", None)
    lesson_name = lesson.get("gh-name", None)
    lesson_date = lesson.get("date", None)              # can be a list
    lesson_start = lesson.get("start-time", None)       # can be a list
    lesson_type = LessonType(lesson.get("type", None))  # have to differentiate between markdown and r-markdown lessons

    if [thing for thing in (lesson_name, lesson_date, lesson_title, lesson_start) if thing is None]:
        raise ValueError(f"gh-name, date, title, and start-time are required for each lesson")

    # Since we allow multiple dates and start times per lesson, we need to be
    # able to iterate over even single values so turn into list. When done,
    # convert the dates from str to datetime.date objects.

    if type(lesson_date) is not list:
        lesson_date = [lesson_date]
    if type(lesson_start) is not list:
        lesson_start = [lesson_start]

    lesson_date = [get_date_object(date) for date in lesson_date]

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
        datestr = lesson_date[i].strftime("%d %B %Y")

        if workshop_start_date and lesson_date[i] < workshop_start_date:
            raise ValueError(f"The date for {lesson_name} day {i + 1} is before the workshop start date")
        if workshop_end_date and lesson_date[i] > workshop_end_date:
            raise ValueError(f"The date for {lesson_name} day {i + 1} is after the workshop end date")

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
            <h4>{datestr}</h4>
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

    if lesson_type == LessonType.markdown:
        start_time = get_time_object(lesson_start[0])
        start_time_minutes = start_time.hour * 60 + start_time.minute
        write_detailed_lesson_schedule(lesson_name, start_time_minutes)

write_overall_schedule(html_schedules)
