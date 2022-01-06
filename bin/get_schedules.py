"""Create schedule for the workshop.

Determines which lesson schedules are required by reading _config.yml. The
schedule for each lesson is modified by a delta time to account for different
start times to what is in the schedule. The schedules are written to HTML in an
(n x 2) array, with the first column being filled first (in date order) just
like in an academic journal. This script updates _includes/rsg/schedule.html,
and creates a detailed 00-schedule.md file for each lesson.
"""

import datetime
import yaml
import math
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
        The string of the date, in format YYYY-MM-DD. But any which dateutil
        accepts is also acceptable.

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

    If unable to parse the string, a ValueError exception is raised as we
    cannot continue when there are missing time objects.

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

def create_detailed_lesson_schedules(lesson_name, lesson_type, start_time):
    """Create a detailed lesson schedule landing page for each lesson.

    The schedule is based on a modifed version of syllabus.html to work better
    with the workshop format. This function also renames the ordering of
    lessons, so the schedule will always be lesson 00.

    Parameters
    ----------
    lesson_name: str
        The name of the lesson.
    lesson_type: LessonType
        The type of lesson.
    start_time: str
        The start time of the lesson.
    """
    if lesson_type == LessonType.markdown:
        file_ext = "md"
        containing_directory = f"collections/_episodes/{lesson_name}-lesson"
    else:
        containing_directory = f"collections/_episodes_rmd/{lesson_name}-lesson"
        file_ext = "Rmd"

    for i, file in enumerate(sorted(glob.glob(f"{containing_directory}/[0-9]*.{file_ext}"))):
        filepath = Path(file)
        new_file_name = f"{i + 1:02d}{filepath.stem.lstrip(string.digits)}.{file_ext}"
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


def create_index_schedules(schedules):
    """Write the new schedule to _includes/rsg/schedule.html.

    The schedules which are passed are ordered by the date of the lessons, and
    are displayed in a two column format. The first column is filled up first,
    followed by the second column.

    Parameters
    ----------
    schedules: list[dict]
        The list of schedules to write to the file. Each schedule is a dict
        with keys "date" which is the date for the lesson and "schedule" which
        is the html table for the schedule.
    """
    html = "<div class=\"row\">"
    n_lessons = len(schedules)
    n_rows = math.ceil(n_lessons / 2)
    ordered_schedules = sorted(schedules, key=lambda x: x["date"])

    for i in range(n_rows):
        left_idx = i
        html += ordered_schedules[left_idx]["schedule"]

        right_idx = i + n_rows
        if right_idx < n_lessons:
            html += ordered_schedules[right_idx]["schedule"]

    html += "</div>"

    with open("_includes/rsg/schedule.html", "w") as fp:
        fp.write(bs(html, "html.parser").prettify())


def main():
    """Main function of the script.

    Handles all of the top level logic, for iterating through lessons to create
    the schedule HTML. Each lesson (and day) schedule is placed into an list,
    which is put into date order and written to HTML. Additionally, this script
    also creates a 00-schedule.md file for each lesson, which is used to create
    a detailed syllabus.
    """
    website_config = get_yaml_config()

    # Try to parse the start and end date for the workshop, to check that lessons
    # are in the correct time frame. If the date is not a valid date, i.e. if it
    # still says FIXME, then we do not check the start and end date.

    workshop_start_date = get_date_object(website_config.get("startdate", None))
    workshop_end_date = get_date_object(website_config.get("enddate", None))

    # Iterate over each lesson, to add their schedule to the html_schedules string

    lessons = website_config.get("lessons", None)
    if not lessons:
        raise ValueError("No lessons found in the workshop configuration file (_config.yml)")
    lesson_schedules = []

    for lesson in lessons:
        lesson_type = LessonType(lesson.get("type", None))  # have to differentiate between markdown and r-markdown lessons
        lesson_title = lesson.get("title", None)
        lesson_name = lesson.get("gh-name", None)
        lesson_dates = lesson.get("date", None)             # can be a list
        lesson_starts = lesson.get("start-time", None)      # can be a list

        if [thing for thing in (lesson_name, lesson_dates, lesson_title, lesson_starts) if thing is None]:
            raise ValueError(f"gh-name, date, title, and start-time are required for each lesson")

        # Since we allow multiple dates and start times per lesson, we need to be
        # able to iterate over even single values so turn into list. When done,
        # convert the dates from str to datetime.date objects.

        if type(lesson_dates) is not list:
            lesson_dates = [lesson_dates]
        if type(lesson_starts) is not list:
            lesson_starts = [lesson_starts]

        lesson_dates = [get_date_object(date) for date in lesson_dates]

        # Get the schedule(s) for the lesson into a dataframe and also the html
        # so we can search for the permalinks

        with open(f"_includes/rsg/{lesson_name}-lesson/schedule.html", "r") as fp:
            schedule_html = fp.read()

        soup = bs(schedule_html, "html.parser")
        all_schedules = pandas.read_html(schedule_html, flavor="lxml")

        if len(all_schedules) != len(lesson_dates):
            raise ValueError(f"There are not the same number of lesson dates for the number of schedules for"
                              " {lesson_name} lesson")
        if len(all_schedules) != len(lesson_starts):
            raise ValueError(f"There are not the same number of lesson start times for the number of schedules for"
                              " {lesson_name} lesson")

        # Loop over each schedule table, if the lesson has multiple schedules

        for i, schedule in enumerate(all_schedules):

            schedule.columns = ["time", "session"]
            permalink = soup.find_all("a", href=True)[i]["href"]  # assume each table has a permalink to a lesson
            start_time = get_time_object(lesson_starts[i])
            original_start = get_time_object(schedule["time"][0])
            datestr = lesson_dates[i].strftime("%d %B %Y")

            if workshop_start_date and lesson_dates[i] < workshop_start_date:
                raise ValueError(f"The date for {lesson_name} day {i + 1} is before the workshop start date")
            if workshop_end_date and lesson_dates[i] > workshop_end_date:
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

            lesson_schedules.append({"date": lesson_dates[i], "schedule": table})

        start_time = get_time_object(lesson_starts[0])
        start_time_minutes = start_time.hour * 60 + start_time.minute
        create_detailed_lesson_schedules(lesson_name, lesson_type, start_time_minutes)

    create_index_schedules(lesson_schedules)


if __name__ == "__main__":
    main()
