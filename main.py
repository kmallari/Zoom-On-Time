from os import link
import os
import schedule
import time
import webbrowser
from datetime import datetime


def txt_to_list(file_name):
    # CONVERTS LINES FROM FILES TO A 2D ARRAY
    with open(file_name) as f:
        lines = f.readlines()

    # SPLITS EACH INFO ABOUT COURSE
    for i, line in enumerate(lines):
        lines[i] = line.split("\t")

    return lines


def list_to_dict(l):

    # TO BE USED WHEN GETTING INFO FROM LIST
    legend = {
        1: "units",
        2: "title",
        3: "section",
        4: "prof",
        5: "days-time",
        6: "zoom_link",
    }

    temp_dict = {}
    classes_dict = {}

    # STORES TEMP INFO INTO TEMP_DICT AND PLACES THAT INFO
    # INTO classes_dict[course_code]
    for i, course in enumerate(l):
        temp_dict = {
            "units": "",
            "title": "",
            "section": "",
            "prof": "",
            "days-time": "",
            "zoom_link": "",
        }
        for j, info in enumerate(course):
            if j >= 7:
                break
            if j != 0:
                temp_dict[f"{legend[j]}"] = info
        classes_dict[l[i][0]] = temp_dict

    # SPLITS THE DAYS-TIME VALUE INTO TWO INDIVIDUAL KEY-VALUE PAIRS
    # AND SPLITS THE DAYS INTO AN ARRAY
    for key in classes_dict.keys():
        classes_dict[key]["days"] = (
            classes_dict[key]["days-time"].split(" ")[0].split("-")
        )
        classes_dict[key]["time"] = classes_dict[key]["days-time"].split(" ")[1]
        del classes_dict[key]["days-time"]

    return classes_dict


# RETURNS A DICTIONARY IN THE FORMAT day: [courses]
def dict_to_days_dict(dict):

    days = ["M", "T", "W", "TH", "F", "SAT"]
    days_dict = {}

    for day in days:
        days_dict[day] = []
        for key in dict.keys():
            if day in dict[key]["days"]:
                days_dict[day].append(dict[key])

    return days_dict


# CONVERTS THE TIME INPUT TO THE APPROPRIATE FORMAT
def format_time(time):
    return time.split("-")[0][0:2] + ":" + time.split("-")[0][2:-1] + "0"


# OPENS THE LINK IN YOUR DEFAULT BROWSER
def open_link(url):
    webbrowser.open_new_tab(url)


# A "SWITCH" STATEMENT FOR ALL THE WORK DAYS.
# THIS FUNCTION SCHEDULES THE OPENING OF THE ZOOM LINKS
def schedule_switch(dict):
    for key in dict.keys():
        if key == "M":
            for course in dict[key]:
                time = format_time(course["time"])
                # print(time)
                schedule.every().monday.at(time).do(open_link, url=course["zoom_link"])
        elif key == "T":
            for course in dict[key]:
                time = format_time(course["time"])
                schedule.every().tuesday.at(time).do(open_link, url=course["zoom_link"])
        elif key == "W":
            for course in dict[key]:
                time = format_time(course["time"])
                schedule.every().wednesday.at(time).do(
                    open_link, url=course["zoom_link"]
                )
        elif key == "TH":
            for course in dict[key]:
                time = format_time(course["time"])
                schedule.every().thursday.at(time).do(
                    open_link, url=course["zoom_link"]
                )
        elif key == "F":
            for course in dict[key]:
                time = format_time(course["time"])
                schedule.every().friday.at(time).do(open_link, url=course["zoom_link"])
        elif key == "SAT":
            for course in dict[key]:
                time = format_time(course["time"])
                schedule.every().saturday.at(time).do(
                    open_link, url=course["zoom_link"]
                )


# PRINTS THE CLASSES EXPECTED TODAY IN ORDER.
# THE CLASS HAPPENING SOON DISPLAYS FIRST,
# AND THE LAST CLASS DISPLAYS LAST.
def print_classes_today(dict):
    days = ["M", "T", "W", "TH", "F", "SAT"]
    day_today = datetime.today().weekday()

    # FROM STACK OVERFLOW
    sorted_courses = sorted(dict[days[day_today]], key=lambda d: d["time"])

    print("YOUR CLASSES TODAY:")

    for course in sorted_courses:
        print(
            f"""Course: {course["title"]}
Units: {course["units"]} | Section: {course["section"]} | Prof: {course["prof"]}
Sync Days: {course["days"]} | Meeting Time: {course["time"]}
Zoom Link: {course["zoom_link"]}
        """
        )


def main():
    # CANCELS ALL ONGOING JOBS
    schedule.clear()

    # CLEARS THE CONSOLE FOR CLEANER LOOK
    os.system("cls" if os.name == "nt" else "clear")

    # DOES THE NECESSARY CONVERSIONS FOR THE PROGRAM
    classes_list = txt_to_list("sched.txt")
    classes_dict = list_to_dict(classes_list)
    days_dict = dict_to_days_dict(classes_dict)
    print_classes_today(days_dict)
    schedule_switch(days_dict)

    print("Auto Class Opener is running...")


if __name__ == "__main__":

    # CALLS THE MAIN FUNCTION
    main()

    # RESETS THE APP IN CASE YOU'RE A MADMAN THAT DOESN'T
    # TURN OFF YOUR PC AND CHANGES NEED TO BE DONE
    schedule.every().day.at("00:00").do(main)

    # RUNS THE SCHEDULED JOBS
    while True:
        schedule.run_pending()
        time.sleep(1)
