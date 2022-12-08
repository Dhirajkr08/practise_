"""
class car:
    speed=0
    color="white"
    no_tyres=4
    def check_distance(self,speed,time):
        print(speed*time)
    def print_attributes(self):
        print(self.color) 
        print(self.speed)
        print(self.no_tyres)
my_car=car()
my_car.speed=140
my_car.color="Black"
my_car.check_distance=(140,60)
my_car.print_attributes()
other_car=car()
other_car.speed=120
other_car.check_distance(120,60)
other_car.print_attributes()
"""

"""
class student:
    def Find_marks(self,name,age,marks,roll):
        self.marks=marks
        self.age=age
        self.roll=roll
        self.name=name
        
    def print_attributes(self):
        print(self.name,self.marks,self.age,self.roll)
        

sdn1=student()
sdn1.name="bunny"
sdn1.marks=92
sdn1.age=25
sdn1.roll=7

sdn1.print_attributes()  """  

"""class student:
    def find_student(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no
    def print_attributes(self):
        print(self.name)
        print(self.roll_no)
sdn1=student()
sdn1.name="John"
sdn1.roll_no=2 
sdn1.print_attributes()  """

"""class triangle:
    def find_perimeter(self,a,b,c):
        s=a+b+c
        print(s)
    def print(self):
        print(self.a) 
        print(self.b)
        print(self.c)   

    def find_area(self,a,b,c):
        s=(a+b+c)/2
        area=(s*(s-a)*(s-b)*(s-c))
        print(area)
    def print_attrbutes(self):
        print(self.a)
        print(self.b)
        print(self.c)
area=triangle()
area.find_area(3,4,5) 
area.find_perimeter(3,4,5)
area.print_attrbutes()         
"""

"""class triangle:
    def find_perimeter(self,a,b,c):
        s=a+b+c
        print(s)
      

    def find_area(self,a,b,c):
        s=(a+b+c)/2
        area=(s*(s-a)*(s-b)*(s-c))
        print(area)
    
area=triangle()
area.find_area(3,4,5) 
area.find_perimeter(3,4,5)"""


"""class Employee:
    def print_details(self,name,year_joining,add):
        print(name,year_joining,add) 
emp1=Employee()
emp1.print_details("Robert",1994,"64C-WallsStreat") 
emp2=Employee()
emp2.print_details("Sam",2000,"68D-WallsStreat") 
emp3=Employee()
emp3.print_details("John",1999,"26B-WallsStreat")        
"""

"""
class Employee:
    def getinfo(self,salary,hrs):
        self.salary=salary
        self.hrs=hrs
    
    def addsal(self):
        if self.salary<500:
            self.salary=self.salary+10
        return self.salary
    def addwork(self):
        if self.hrs>6:
            self.salary=self.salary+5
        return self.salary
    def print_final_salary(self):
        print(self.salary)
salary=int(input("salary:"))
hrs=int(input("hrs:"))
emp1=Employee()
emp1.getinfo(salary,hrs)
emp1.addsal()
emp1.addwork()
emp1.print_final_salary()
"""

"""
class obj_count:
    count=0
    def __init__(self,name,age):
        self.name=name 
        self.age=age 
        obj_count.count=obj_count.count+1
    def print_attributes(self):
        print(self.name,self.age)
sdn1=obj_count("Dhiraj",24)
sdn2=obj_count("Amit",22)
sdn3=obj_count("rahul",25)
print(obj_count.count) 
"""

'''class PARENT:
    def parent_class(self):
        print("this is parent class")
class CHILD(PARENT):
    def child_class(self):
        print("this is child class")
P=PARENT()
P.parent_class() 
C=CHILD()
C.child_class()
C.parent_class()       
'''

'''class member:
    def member_details(self,name,age,ph_no,add,salary):
        print(name,age,ph_no,add)
    def print_salary(self):
        print(self.name)
        print(self.age) 
        print(self.ph_no)
        print(self.address)
        print(self.salary)
class Employee(member):
    def employee_details(self,department,specialization):
        print(self.specialization)
        print(self.department)
class Manager(member):
    def manager_details(self,department,specialization):
        print(self.department)
        print(self.specialization)
e=Employee()
e.employee_details=("bunny",24,9608946773,"xyz","$500","IT","dev")
e.print_salary()
m=Manager()
m.manager_details=("Dhiraj",25,9608946773,"xyz","$800","IT","dev")
m.print_salary()'''

class shape:
    def shape_details(self):
        print("this is shape")
class rectangle:
    def rec_shape(self):
        print("this is rectangle shape")
class circle:
    def cir_shape(self):
        print("this is circular shape")
class square(shape,rectangle):
    def sq_shape(self):
        print("square is rectangle") 
s=square()
s.shape_details() 
s.rec_shape() 
s.sq_shape()                             











            
        
        



