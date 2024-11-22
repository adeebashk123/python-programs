class Teacher:
    def _init(self, name, subject):  # Corrected __init_ method
        self.name = name
        self.subject = subject

    def displayTeacherDetails(self):
        print("Teacher ->  name : ", self.name, " subject : ", self.subject)

class Dancer:
    def _init(self, name, academy):  # Corrected __init_ method
        self.name = name
        self.academy = academy

    def displayDancerDetails(self):
        print("Dancer ->  name : ", self.name, " academy : ", self.academy)

class DanceTeacher(Teacher, Dancer):
    def _init(self,name,subject,academy):  # Corrected __init_ method
        Teacher._init_(self,name,subject)  # Initialize Teacher
        Dancer._init_(self,name,academy)  # Initialize Dancer

danceTeacher1 = DanceTeacher()
danceTeacher1.displayTeacherDetails()
danceTeacher1.displayDancerDetails()