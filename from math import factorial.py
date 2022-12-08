from math import factorial


def recur_factorial(n):
    if n == 1:
        return n 
    else:
        return n*recur_factorial(n-1)
        num =7
        if num < 0:
            print("factorial does not exit with negative numbers")
        elif num == 0:
            print("the factorial of 0 is 1")
        else:
            print("the factorial of ",'num',recur_factorial(num-1))

