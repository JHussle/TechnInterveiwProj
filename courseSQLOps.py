from traceback import print_tb
import connection as c
import mysql.connector

def readCourseInfo():
    conn = c.returnConnection()
    try:
        table = conn.cursor()
        table.execute("use coursetracker")
        table.execute('SELECT * FROM courses')
        for column in table:
            print(f'''
                  Course ID...........{column[0]}
                  Course Name.........{column[1]}
                  Course Status.......{column[2]}
                  Course Created......{column[3]}
                  Course Update.......{column[4]}
                  Course Removeal.....{column[5]}
                  ''')
            table.close()
            conn.close()
    except (Exception, mysql.connector.Error) as error:
        print('Error while fetching data from my MySQL', error)

def insertCourseInfo(course):
    conn = c.returnConnection()
    try:
        cursor = conn.cursor()
        cursor.execute("use coursetracker")
        cursor.execute(
            f"INSERT INTO courses (courseID, courseName, courseStatus, courseCreated, courseUpdate, courseDelete) VALUES ('{course.courseID}', '{course.courseName}', '{course.courseStatus}', '{course.courseCreated}', '{course.courseUpdate}', '{course.courseDelete}')"
        )
        conn.commit()
        cursor.close()
        conn.close()
    except (Exception, mysql.connector.Error) as error:
        print('Error while fetching data from my MySQL', error)
