from cv2 import divide
from numpy import add, multiply,subtract


num1 = float(input("enter a first number"))
num2 = float(input("enter a second number"))
print("operation:+,-,*,/")
select = input("select operations:")
if select == "+":
 print(num1,"+",num2,"=",add(num1,num2))
elif select == "-":
    print(num1,"-",num2,"=", subtract(num1,num2))
elif select == "*":
    print(num1,"*",num2,"=",multiply(num1,num2))
elif select == "/":
    print(num1,"/",num2,"=",divide(num1,num2))
next_calculation = input("let's do next calculation? (yes/no)")
if next_calculation == "no":
     Break
else:
    print("Invalid input")

