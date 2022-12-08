''' Write a Program to create a Class Employee

It contains two attributes -> Name, Salary

Create 5 objects and initialize any random values for Name and Salary to it.

Store all these objects in an Array and print the names of the employees sorted in Descending Order of Salary using any of the sorting mechanism.

(bubble Sort, Insertion Sort or selection Sort).''' 

class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
   
    
           
emp1=employee("Rahul",43000) 
emp2=employee("Gaurav",32000)
emp3=employee("saurav",23000) 
emp4=employee("Amit",31000) 
emp5=employee("ajay",75000) 
employee=[emp1,emp2,emp3,emp4,emp5] 
def find_salary(employee):
    return employee.name and employee.salary
employee.sort(key=find_salary,reverse=True)
for employee in employee:
    print(employee.name,employee.salary)

    









