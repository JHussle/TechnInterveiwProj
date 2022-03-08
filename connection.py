import mysql.connector, os
from mysql.connector import connect

def returnConnection():
    conn = connect(
        host="database-1.cgcvcwhnvywf.us-east-1.rds.amazonaws.com",
        user="admin",
        password="password",
        database = "coursetracker"
    )
    return conn



