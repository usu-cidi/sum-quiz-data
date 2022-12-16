# Summarized Quiz Data Project
Center for Instructional Design and Innovation - Utah State University
* Created by Emma Lynn (a02391851@usu.edu)
* Supervised by Neal Legler, CIDI Director (neal.legler@usu.edu)
* On request from Jackson Graham, Mechanical and Aerospace Engineering Dept.

**_Documentation of progress on the project_**

## Project Goals
* Generate a report showing summarized data for each quiz in several specified sections of a specified course
* Get data for all quizzes in course
* Output a .csv in approved format
  * Headers: Quiz Name, Quiz ID, Avg time spent (per student), Avg num attempts made (per student), Avg score, num students who took the quiz (possibly divided by section?)

### Data to retrieve
* For each specified section of a specified course:
  * For all quizzes in a course
    * For each student
      * Add to average score
      * Add to number of students who took it
      * Add to number of attempts made
      * For each attempt
        * Add to average time spent


## Progress Report

### 12.13.22
* Copied over from Individual Quiz Data project
* Began making relevant changes

### 12.15.22
* Took out student info api call
* Reformatted data
* Threw out quiz times that were longer than 4 hours (14400 seconds)
* Updated documentation
* Began running on Jackson's courses
* Moved to public repository

### 12.16.22
* Fixed a divide by zero error that occurs when a quiz is worth 0 points
* Fixed a bug with throwing out data that has timed out
* Ran on Jackson's courses, got the data, I'll combine them tomorrow


### TODO
* Check on number of students

## Bug reports / maintenance

### Placeholder
00.00.00
Reported by -
```buildoutcfg
error
```

## Sources:
* 