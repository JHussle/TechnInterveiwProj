# Course Object
class Course:
    #Class Attributes
    courseInfo = 4
    #initializer
    def __init__(self, courseID, courseName, courseStatus, courseCreatedAt, courseUpdatedAt, courseDeletedAt):
        self.courseID = courseID
        self.courseName = courseName
        self.courseStatus = courseStatus
        self.courseCreatedAt = courseCreatedAt
        self.courseUpdatedAt = courseUpdatedAt
        self.courseDeletedAt = courseDeletedAt