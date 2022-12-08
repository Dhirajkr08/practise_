from operator import methodcaller
from tkinter import N


"""def day_name(day):
    n={1:"monday",2:"tuesday",3:"wednesday",4:"thursday",5:"friday",6:"saturday",7:"sunday"}
    return n.get(day)
def main():
    day=int(input())
    print(day_name(day))
main() """

#2nd method
def day_name(day):
    if day==1:
        print("monday")
        
    elif day==2:
        print("tuesday")
    elif day==3:
        print("wednesday")
    elif day==4:
        print("thursday")
    elif day==5:
        print("friday")
    elif day==6:
        print("saturday")
    elif day==7:
        print("sunday")
    else:
        print("day is not valid")
def main():
    day=int(input())
    day_name(day)
main()                                   


