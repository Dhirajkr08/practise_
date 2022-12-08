class Employee():
    def getinfo(self,salary,hours):
        self.salary=salary
        self.hours=hours
    def addsal(self):
        if self.salary<500:
            self.salary=self.salary+10
        return self.salary
    def addwork(self):
        if self.hours>6:
            self.salary=self.salary+5
        return self.salary
    def finalSalary(self):
        print(self.salary)
salary=int(input("Enter your salary ="))
hours=int(input("enter the working hour ="))        
emp1=Employee()
emp1.getinfo(salary,hours) 
emp1.addsal() 
emp1.addwork()
emp1.finalSalary()                         