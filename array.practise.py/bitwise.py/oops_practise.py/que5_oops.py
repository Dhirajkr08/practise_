class c_obj:
    count=0
    def __init__(self,name,age):
        self.name=name
        self.age=age
        c_obj.count=c_obj.count+1
    def show_details(self):
        print(self.name,self.age)
p=c_obj("DHiraj",25)
p1=c_obj("Bunny",25)
p2=c_obj("Rohit",38) 
print(c_obj.count)           


