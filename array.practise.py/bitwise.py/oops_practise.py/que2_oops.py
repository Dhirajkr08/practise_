class triangle:
    def find_perimeter(self,a,b,c):
        perimeter=a+b+c
        print(perimeter)
    def find_area(self,a,b,c):
        perimeter=(a+b+c)/2
        area=(perimeter*(perimeter-a)*(perimeter-b)*(perimeter-c) )
        print(area)
perimeter=triangle() 
perimeter.find_perimeter(3,4,5)
area=triangle()
perimeter.find_area(3,4,5)          