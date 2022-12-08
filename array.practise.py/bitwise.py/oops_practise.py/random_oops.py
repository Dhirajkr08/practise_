class member():
    def __init__(self,name,age,number,address,salary):
        self.name=name
        self.age=age
        self.number=number
        self.address=address
        self.salary=salary
    def PrintSalary(self):
        print(self.salary)
class Employee(member):
    def __init__(self,name,age,number,address,salary,specialzation):
        self.specialization=specialzation
        super().__init__(name,age,number,address,salary)
class Manager(member):
    def __init__(self, name, age, number, address, salary,department):
        super().__init__(name, age, number, address, salary)
        self.department=department
e=Employee("dj",24,"xyz","pat",45000,"abc")
m=Manager("Dhiraj",24,"YYYY","PAt",95000,"CCC")
e.PrintSalary()
m.PrintSalary()                            