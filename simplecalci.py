from secrets import choice
from select import select


def add(x,y):
    return x+y
def substract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide (x,y):
    return x/y
print("select operation.")
print("1.add")
print("2.substract")
print("3.multiply")
print("4.divide")
num1 = float (input("enter the first number:"))
num2 = float(input("enter the second number:"))
print("operation:1,2,3,4")
choice = input("choose operations")
if choice == '1':
    print(num1,"+",num2,"=",add(num1,num2))
elif choice == '2':
    print(num1,"-",num2,"=",substract(num1,num2))
elif choice == '3':
    print(num1,"*",num2,"=",multiply(num1,num2))
elif choice == '4':
    print(num1,"/",num2,"=",divide(num1,num2))
    next_calculation = input("let's do next calculation?(yes/no):")
if next_calculation == "no":
    break
else:
    print("invalid input")   
