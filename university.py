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
  
class OtherStaff(Staff):
    def __init__(self,university,first_name, last_name, age,position):
        super().__init__(university,first_name, last_name, age)
        self.position = position
       
    def more_info(self):
        print(f"University: {self.university} Staff Name: {self.first_name} Last Name: {self.last_name} Position: {self.position}")
class Object(University):
    def __init__(self, university,name):
        super().__init__(university)
        self.name = name
        
    def more_info(self):
        print(f"University: {self.university} Name: {self.name} ")

class Computer(Object):
    def __init__(self,university,name,soni, tizimi, holati):
        super().__init__(university,name)
        self.soni = soni
        self.tizimi = tizimi
        self.holati = holati
        
    def more_info(self):
        print(f"University: {self.university} Name: {self.name} Soni: {self.soni} Tizimi: {self.tizimi} Holati: {self.holati}")

class Mebel(Object):
    def __init__(self,university,name,soni, turi, holati):
        super().__init__(university,name)
        self.soni = soni
        self.turi = turi
        self.holati = holati
        
    def more_info(self):
        print(f"University: {self.university} Name: {self.name} Soni: {self.soni} Turi: {self.turi} Holati: {self.holati}")
         
# uni = University("Tatu")
# uni.info()

# staff = Staff("Tatu","Omon", "Omonov", 22)
# staff.more_info()

# stud = Student("Tatu","Omon", "Omonov", 22, "A")
# stud.more_info()

# stud = Teacher("Tatu","Omon", "Omonov", 22, "Star", "Sub")
# stud.more_info()

# o_staff = OtherStaff("Tatu","Omon", "Omonov", 22, "Star")
# o_staff.more_info()

# obj = Object("Tatu","Omon")
# obj.more_info()

# comp = Computer("Tatu","Omon", 250, "Windows", "Yaxshi")
# comp.more_info()

meb = Mebel("Tatu","Omon", 250, "Krovat", "Yaxshi")
meb.more_info()

