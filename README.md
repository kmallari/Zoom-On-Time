# Zoom-Opener
A C++ application that opens the zoom link of your class 2 minutes before the class time.

# How to use
First, make a text file called "classes.txt".

Put your classes there in the format. Separate each course with a comma and separate each detail about the course with a space.:
|Course Name|Days of the Class|Time|Zoom Link|      
|----|-----|-------|-----------|      

Here is an example .txt file:
```
Circuits_I Mon|Tue|Wed 10:00 https://zoom.us/classLinkHere,
Electronics_I Sat 13:00 http://zoom.us/classLinkHere,
Software_Dev Thu 15:00 http://zoom.us/classLinkhere,
```

If the class is held on multiple days of the week, separate each day with `|`.

Make sure to use military time format for the time and separate the hours and minutes with a `:`.

Once you're done making the "classes.txt" file, you can compile the .cpp file.
