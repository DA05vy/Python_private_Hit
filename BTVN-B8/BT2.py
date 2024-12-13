class Person:
    def __init__ (self, name, yob:int):
        self.name = name
        self.yob = yob
    def describe(self):
        print(f"Name= {self.name} - YoB= {self.yob}", end = '')

class Student(Person):
    def __init__(self, name, yob, grade):
        super().__init__(name,yob)
        self.grade = grade
    def describe(self):
        print(f"Student - ", end = '')
        super().describe()
        print(f" - Grade= {self.grade}")

class Teacher(Person):
    def __init__(self, name, yob, subject):
        super().__init__(name,yob)
        self.subject = subject
    def describe(self):
        print(f"Teacher - ", end = '')
        super().describe()
        print(f" - Subject= {self.subject}")
        
class Doctor(Person):
    def __init__(self, name, yob, specialist):
        super().__init__(name,yob)
        self.specialist = specialist
    def describe(self):
        print(f"Doctor - ", end = '')
        super().describe()
        print(f" - Specialist= {self.specialist}")      

class Ward:
    def __init__(self, name):
        self.name = name
        self.list = []
    def addPerson(self, p: Person):
        self.list.append(p)
    def describe(self):
        for i in self.list:
            i.describe()
    def countDoctor(self): 
        #i là một the hien cua lop Teacher (hoac la mot lop con cua Teacher), thi isinstance(i, Teacher) tra ve True.
        dem = sum ( 1 for i in self.list if isinstance(i, Doctor))
        return dem
    def sortAge(self):
        #lay gia tri yob cho moi phan tu trong danh sach de sap xep
        sorted_list = sorted(self.list, key=lambda person: person.yob)
        # for person in sorted_list:
        #     person.describe()
    def aveTeacherYoB(self):
        teachers = [i.yob for i in self.list if isinstance(i,Teacher)]
        if len(teachers) > 0:
            return sum(teachers)/len(teachers)
        else:
            return None
        

# 2(a)
student1 = Student(name="studentA", yob=2010, grade="7")
student1.describe()

teacher1 = Teacher(name="teacherA", yob=1969, subject="Math")
teacher1.describe()

doctor1 = Doctor(name="doctorA", yob=1945, specialist="Endocrinologists")
doctor1.describe()

# 2(b)
print()
teacher2 = Teacher(name="teacherB", yob=1995, subject="History")
doctor2 = Doctor(name="doctorB", yob=1975, specialist="Cardiologists")
ward1 = Ward(name="Ward1")
ward1.addPerson(student1)
ward1.addPerson(teacher1)
ward1.addPerson(teacher2)
ward1.addPerson(doctor1)
ward1 . addPerson(doctor2)
ward1.describe()