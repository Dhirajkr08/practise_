class Employee:
    def employee_details(self,name,year_of_joining,address):
        self.name=name
        self.year=year_of_joining
        self.address=address
    def show_employee(self):    
        print(self.name,self.year,self.address)
emp1=Employee()
emp1.employee_details("Robert",1994,"64C-WallsStreat") 
emp1.show_employee()
emp2=Employee()
emp2.employee_details("Sam",2000,"68D-WallsStreat")
emp2.show_employee()
emp3=Employee()
emp3.employee_details("John",1999,"26B-WllsStreat")
emp3.show_employee()