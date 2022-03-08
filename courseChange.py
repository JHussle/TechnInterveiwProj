class CourseChange:
    def __init__(self, courseNum, courseName, courseState):
        self.courseNum = courseNum
        self.courseName = courseName
        self.courseState = courseState
        
    def set_courseNum(self, courseNum):
        self.__courseNum = courseNum
    def get_courseNum(self):
        return self.__courseNum
    
    def set_courseName(self, courseName):
        self.__courseName = courseName
    def get_courseName(self):
        return self.__courseName
    def set_courseState(self, courseState):
        self.__courseState = courseState
    def get_courseState(self):
        return self.__courseState