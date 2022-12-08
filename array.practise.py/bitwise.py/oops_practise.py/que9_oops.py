class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
e5=Employee("DHiraj",45000)
e1=Employee("Bunny",49000)
e2=Employee("Harsh",39000)
e3=Employee("Gaurav",36000)
e4=Employee("Saurav",39000)
Employee=[e1,e2,e3,e4,e5]

def sorted_employee(Employee):
    return Employee.name and Employee.salary
Employee.sort(key=sorted_employee,reverse=True)
for Employee in Employee:
    print(Employee.name,Employee.salary)

    
