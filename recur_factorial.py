def recur_factorial(n):
    if n == 1:
        return n
    else:
        return n*recur_factorial(n-1)
        num=7
        if num < 0 :
            print("the factorial number does not exist for negative number")
        elif num == 0:
            print("the factorial of 0 is 1")
        else:
            print("the factorial of",num, "is",recur_factorial(num))             