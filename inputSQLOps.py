import sys
import courseSQLOps as sql
from os import system
from course import Course
system('clear')

def listCourseOp():
    sql.readCourseInfo
    
courses = []

def inputCourseInfoOps():
    courseID = input("Enter Course ID: ")
    courseName = input("Enter Course Name: ")
    courseStatus = input("Enter Course Status: ")
    while True:
    ## statement for course information should be returned with time/date
    
    course = Course(courseID, courseName, courseStatus)
    
    sql.insertCourseInfo(course)
inputCourseInfoOps()