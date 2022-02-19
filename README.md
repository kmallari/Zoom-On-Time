# Zoom-Opener
A Python application that opens the zoom link of your class on the class time.

# How to use
First, make a text file called "sched.txt".

Put your classes there in the format. Separate each info with a tab and put each course in one line.:
|Course Code |Course Name|Section|Name of Professor|Schedule|Zoom Link|      
|----|-----|-------|-----------|----|-

Here is an example `sched.txt` file:
```
CLASS CODE 10.2	UNITS	COURSE NAME	SECTION	PROFESSOR, NAME OF	T 1400-1530 / TBA	https://zoom.us/link
CSCI 20	3	COMPUTER SCIENCE BASICS	A	PAUL, JEAN	T-TH 0800-0930 / TBA	https://zoom.us/link

```

After making the schedule file, make sure to install the dependency in `requirements.txt`.
You can now run the application using `py main.py`.
