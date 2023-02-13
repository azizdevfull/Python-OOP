class University:
    def __init__(self, university):
        self.university = university
        
    def info(self):
        print(f"University: {self.university}")
        
class Staff(University):
    def __init__(self, university,first_name, last_name, age):
        super().__init__(university)
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        
    def more_info(self):
        print(f"University: {self.university} Staff Name: {self.first_name} Last Name: {self.last_name} Age: {self.age}")

class Student(Staff):
    def __init__(self,university,first_name, last_name, age,group):
        super().__init__(university,first_name, last_name, age)
        self.group = group
        
    def more_info(self):
        print(f"University: {self.university} Staff Name: {self.first_name} Last Name: {self.last_name} Age: {self.age} Groups: {self.group}")

class Teacher(Staff):
    def __init__(self,university,first_name, last_name, age,position, subject):
        super().__init__(university,first_name, last_name, age)
        self.position = position
        self.subject = subject
       
    def more_info(self):
        print(f"University: {self.university} Staff Name: {self.first_name} Last Name: {self.last_name} Position: {self.position} Subject: {self.subject}")
  
            
# uni = University("Tatu")
# uni.info()

# staff = Staff("Tatu","Omon", "Omonov", 22)
# staff.more_info()

# stud = Student("Tatu","Omon", "Omonov", 22, "A")
# stud.more_info()

stud = Teacher("Tatu","Omon", "Omonov", 22, "Star", "Sub")
stud.more_info()