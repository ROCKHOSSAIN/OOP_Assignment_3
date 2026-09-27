class Student():
    def __init__(self,name,student_id,email,age,department,marks):
        self.name=name
        self.id=student_id
        self.__email=email
        self.age=age
        self.department=department
        self.__marks=marks
    @property
    def get_email(self):
        return self.__email
    @property
    def get_marks(self):
        return self.__marks
    
    @get_email.setter
    def get_email(self,email):
        if "@" in email:
            self.__email=email
        else:
            print("email is not correct way")
        

    @get_marks.setter
    def get_marks(self,marks):
        if(0<=marks<=100):
            self.__marks=marks
        else:
            print("number is out of range!!")
    def calculate_result(self):
        if  self.__marks >= 80:
            grade = "A+"
        elif self.__marks >= 70:
            grade = "A"
        elif self.__marks >= 60:
            grade = "B"
        elif self.__marks >= 50:
            grade = "C"
        elif self.__marks >= 40:
            grade = "D"
        else:
            grade = "Fail"
        return grade
    
    

    def display_info(self):
        print(f"┌{'─' * 45}┐")
        print(f"│  Name       : {self.name:<29} │")
        print(f"│  ID         : {self.id:<29} │")
        print(f"│  Email      : {self.__email:<29} │")
        print(f"│  Age        : {self.age:<29} │")
        print(f"│  Department : {self.department:<29} │")
        print(f"│  Marks      : {self.__marks:<29} │")
        print(f"│  Grade      : {self.calculate_result():<29} │")
        print(f"│  Student Type: {self.get_student_type():<29} │")


        if hasattr(self,"semester"):
            print(f"│  Semester   : {self.semester:<29} │")
        if hasattr(self, 'research'):
            print(f"│  Research   : {self.research:<29} │")

    def get_student_type(self):
        return "Student"



class UndergraduateStudent(Student):
    def __init__(self,semester,*args):
        super().__init__(*args)
        self.semester=semester
    def get_student_type(self):
        return "Undergraduate Student"
        


class GraduateStudent(Student):
    def __init__(self,research_topic,*args):
        super().__init__(*args)
        self.research=research_topic
        

    def get_student_type(self):
        return "Graduate Student"



student1=UndergraduateStudent(5,"rocky",1200,"rockyhossain525@gmail.com",24,"EEE",85)
student1.display_info()
student1.calculate_result()
student1.get_email="exam123@gmail.com"
student1.display_info()

# print(student1.get_student_type())

student2=GraduateStudent("Machine learning and AI","Faizu",1200,"faizu333@yahoo.com",26,"CSE",66)
student2.display_info()
student2.calculate_result()
student2.get_marks=101
student2.display_info()

# print(student2.get_student_type())




