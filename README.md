# IS 3020 Final Project

## Student and Project Information

- Student name: Tyler Young
- GitHub username: tyoun100
- Project title: Class Schedule Builder
- Application purpose: To create a master schedule for multiple classes in one location.

## How to Run the Application

Explain the required Python version, required files, and the exact steps for starting the application in PyCharm.

This file runs on Python 3.14. There are no required files, but various inputs will be required. To start, you will
input the requested information, such as class name, course number, professor name, building number or online, and room
number if anything but online is entered. From there, you will either add another class or move onto data inputs. You 
will select the class and copy/paste the course schedule, followed by 'DONE'. You can select another class or move on to
the printed schedule. You can then change the status from pending to completed as you complete each assignment throughout
the semester.

This is known to function for a copy/paste of IS 3020 Week 1 through Lab 10 with one line (project planning) split. 
It is known to function for course schedules listing only due date and assignment name in any order.

## Major Features

List the major user-facing features implemented in the final application.

Classes are printed in the run screen separately and sorted by due date.
Data input is stripped of keywords and certain explanations/sentence structure.
Data is defaulted to pending status.
Data is saved to a CSV and updated with each status change.
The CSV is a combination of every class and assignment in order of due date.

## Python Concepts Used

Explain how the application uses functions, collections, conditionals, loops, file persistence, and exception handling.

Functions: Uses saving to and reading from a CSV to reuse and update existing data. Uses data sorting (by date).
Collections: Uses various lists to hold classes and schedules. Uses dictionaries to hold class data, keywords for removal
and grouped schedules.
Loops: Uses while loops to manage multi-line inputs and maintaining a running loop. Uses for loops to process CSV, output
and more.
File Persistence: Uses CSV writer and dictionary to read from and write to the master schedule, maintaining data 
continuously.
Exception handling: Try/Except are used to prevent crashing from errors with user inputs and missing files. 

## Data Files

Describe each CSV or JSON file and provide a brief explanation of its fields.
CSV file is created from the user inputs after the schedule is stripped (from what I can) and sorted by due date. The 
CSV maintains the following headers: Class name, class number, due date, assignment and status. The CSV is a combination
of every class and every assignment, in order by due date.

## Testing Summary

Describe the major scenarios tested, including invalid input and file-related errors.

I tested IS 3020 course schedule from week 1 through lab 10. The data following that still poses difficult with stripping
'what to work on' and 'final project work' text box being split.
Errors:
Date Jun 3-7 was excluded. I adjusted the code to include this.
Copying further down included 'what to work on' parts with / in the description. I adjusted the code to not crash by
only using / for date if it's .isdigit.
Module 1 was separated from its description by the table formatting I copied from. I merged them based on word count/len
and pending module to remove the unnecessary assignment lines.
There were many errors with loops breaking from inputs and CSV. Many of these were solved with correct indentations and 
proper placement of ().

I tested another class with a course schedule only having assignment, date (Personal Video Introduction  Wednesday 6/3).
Errors:
Early code was meant for inputs of date first. I adjusted it to anywhere on the line to move the date to the front.
This class also listed days of the week assignments were due. I removed days of the week from every line.

The last error I encountered was the load function. I wrote the read and write functions at the bottom. I am not sure if
they would function the same if at the top. I tried to add the load function there and the load data list at the top.
It had a definition error because the rest of the function was below it. I moved them to the top, and the save function
then had the same error. I chose to comment it out to prevent the rest of the code from breaking as it works well with
basic inputs, except loading after the program is ended.

## AI Use

Complete `AI_USAGE.md` and summarize the most important AI-assisted improvements here.

AI usage was primarily used as a means for error correction. It was not very helpful in many cases because it wanted to
overcomplicate the script in ways I could not understand. It also gave me incorrect solutions too often. It was helpful
in some cases where my indent was off by one, or I was missing a (). The primary improvements I used from it was the
introduction of iteration (i) to identify the date anywhere on the line and move it to the front. I quickly understood
how it functioned, although it will likely be considered too advanced. AI also assisted with smaller adjustments to allow
CSV reading and writing to work better as I used the wrong words occasionally. It also introduced '\t' to identify tabs
in my input that I could remove. I mostly learned AI is useful for hints, but it will not get you where you need to go.
The information it gives may give you an insight to how to complete the function, and it may show you exactly what to
avoid.