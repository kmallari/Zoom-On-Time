# Zoom On Time
A Python application that opens the zoom link of your class on the class time.

# How to use
**1.** Make a text file called "sched.txt" in the same folder as `main.py`.

**2.** Put your classes there in the format below. Separate each info with a tab and put each course in one line:

|Course Code |Course Name|Section|Name of Professor|Schedule|Zoom Link|      
|----|-----|-------|-----------|----|-

Here is an example `sched.txt` file:
```
CLASS CODE 10.2	UNITS	COURSE NAME	SECTION	PROFESSOR, NAME OF	T 1400-1530 / TBA	https://zoom.us/link
CSCI 20	3	COMPUTER SCIENCE BASICS	A	PAUL, JEAN	T-TH 0800-0930 / TBA	https://zoom.us/link
```

Note: If your class occurs more than once a week, separate each day with a `-`. This is done in the second line of the example above.

Legend for the days in `sched.txt`:
|Full Name | Shorthand|
|---|---|
|Monday|M|
|Tuesday|T|
|Wednesday|W|
|Thursday|Th|
|Friday|F|
|Saturday|SAT|

**4.** After making the schedule file, make sure to install the dependency in `requirements.txt`. Or, just do `pip install schedule`. You can now run the application using `py main.py`.
