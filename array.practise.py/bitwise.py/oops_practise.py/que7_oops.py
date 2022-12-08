class Member:
    def __init__(self,name,age,number,address,salary):
        self.name=name
        self.age=age
        self.number=number
        self.address=address
        self.salary=salary
    def PrintSalary(self):
        print(self.salary)
class Employee(Member):
    def __init__(self, name, age, number, address, salary,specialization):
        self.specialization=specialization
        
        super().__init__(name, age, number, address, salary) 
class Manager(Member):
    def __init__(self, name, age, number, address, salary,department):
        self.department=department
        super().__init__(name, age, number, address, salary)
        
        
            
E=Employee("Dj",24,123,"Pat",34000,"xyz")
m=Manager("DHIRAJ",24,123,"XYZ",98000,"development")
E.PrintSalary() 
m.PrintSalary()                        