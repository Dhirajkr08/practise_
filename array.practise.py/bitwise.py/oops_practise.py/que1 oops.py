class triangle:
    def find_perimeter(self,a,b,c):
        p=(a+b+c)
        print(p)
    def find_area(self,a,b,c):
        p=(a+b+c)/2
        area=p*(p-a)*(p-b)*(p-c)
        print(area)
perimeter=triangle()
perimeter.find_perimeter(3,4,5) 
area=triangle()
area.find_area(3,4,5)
           