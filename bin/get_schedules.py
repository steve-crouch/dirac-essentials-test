"""Create schedule for the workshop.

Reads the lessons.yml configuration file to determine the lessons, then parses
the schedules from each lesson and adds a delta time to the start time of each
schedule depending on the start time of the lesson. The scheduled for each
lesson are then put into a single schedule (split by tables) and written to
the main schedule.html file.
"""

import datetime
import yaml
import pandas
from bs4 import BeautifulSoup as bs

html_template = "<div class=\"row\">"  # Start of the HTML template

# Read the yaml file containing the lesson configuration

with open("_config.yml", "r") as f:
    lesson_config = yaml.load(f, yaml.Loader)

# Go through each lesson to get and update the schedule, depending on start time

for lesson in lesson_config["lessons"]:

    lesson_title = lesson.get("title", None)
    lesson_name = lesson.get("gh-name", None)
    lesson_date = lesson.get("date", None)              # can be a list
    lesson_start_time = lesson.get("start-time", None)  # can be a list

    if [thing for thing in (lesson_name, lesson_date, lesson_title, lesson_start_time) if thing is None]:
        raise ValueError(f"gh-name, date, title, and start-time are required for each lesson")

    # Get the schedule for the lesson into a panadas dataframe, and then figure
    # stuff out

    with open(f"_includes/rsg/{lesson_name}-lesson/schedule.html", "r") as fp:
        schedule_html = fp.read()
    schedule_tables = pandas.read_html(schedule_html, flavor="bs4")  # reads in multiple tables, for multi-day lessons
    html_soup = bs(schedule_html, "html.parser")  # maybe this could be more efficient? :)

    # Change things to a list, if they are not already so we can loop over them

    if type(lesson_date) is not list:
        lesson_date = [lesson_date]
    if type(lesson_start_time) is not list:
        lesson_start_time = [lesson_start_time]

    # Loop over each schedule table, if the event is multi-day

    for i, schedule_table in enumerate(schedule_tables):
        schedule_table.columns = ["time", "session"]
        lesson_permalink = html_soup.find_all("a", href=True)[i]["href"]  # assume each table has a link to the lesson

        this_lesson_start_time = lesson_start_time[i]
        this_lesson_date = lesson_date[i]

        # There is some sorcery required to mangle start-time into a datetime
        # object, depending on how it is written. Examples of the different
        # formats are inline with how we deal with them below.

        if type(this_lesson_start_time) is str:
            try:
                start_time = datetime.datetime.strptime(this_lesson_start_time, "%I:%M %p")  # start-time: 9:30 am
            except ValueError:
                start_time = datetime.datetime.strptime(this_lesson_start_time, "%H:%M")     # start-time: "9:30"
        elif type(this_lesson_start_time) is int:
            hours, minutes = divmod(this_lesson_start_time, 60)
            start_time = datetime.datetime.strptime(f"{hours}:{minutes}", "%H:%M")      # start-time: 9:30
        else:
            raise ValueError(f"start-time {this_lesson_start_time} for lesson \"{lesson['title']}\" is invalid format")

        # Calculate the time difference between the start time, and the start
        # time in the original schedule. This delta time (in minutes) is added
        # to each time in the original schedule

        original_start_time = datetime.datetime.strptime(schedule_table["time"][0], "%H:%M")
        delta_start = start_time - original_start_time
        delta_minutes = divmod(delta_start.total_seconds(), 60)[0]

        # Construct the schedule table for this lesson, adding delta_minutes to
        # each original entry, and add the schedule table to the html template

        table = f"""
        <div class="row">
            <div class="col-md-6">
                <a href="{lesson_permalink}"><h3>{lesson_title}</h3></a>
                <h4>{this_lesson_date}</h4>
                <table class="table table-striped">
        """

        for time, session in zip(schedule_table["time"], schedule_table["session"]):
            actual_time = datetime.datetime.strptime(time, "%H:%M") + datetime.timedelta(minutes=delta_minutes)
            table += f"<tr> <td> {actual_time.hour:02d}:{actual_time.minute:02d} </td>    <td> {session} </td> </tr>\n"

        table += """
                </table>
            </div>
        </div>
        """

        html_template += table

# Finish off the template and use BeautifulSoup to write a pretty version of
# the html file (which is not that pretty, actually)

html_template += "</div>"
pretty_table = bs(html_template, "html.parser").prettify()
with open("_includes/rsg/schedule.html", "w") as fp:
    fp.write(pretty_table)
