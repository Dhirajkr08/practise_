"""n=int(input())
m=int(input())
for i in range(1,m):
    if i==m:
        break
    print(i)"""

"""def print_pattern(n):
    Function to print the pattern
    i = 1
    while i <= n :
        j = n
        string=" "
        while j >= i:
         # printing stars
           string=string+"*"
           j = j - 1
        print(string)
        i = i + 1


    
            
    
   
    
    

n=int(input())
for i in range(n):
    for j in range(i+1):
        print("*",end="")
    print()
for i in range(4,n):    
    for j in range(i+1):
        print("*",end="")
    print()

'''n=int(input())
for i in range(1,n+1):
    
    for j in range(3,n*2):
        if j<=i or j>=n*2-i:
            print("*",end="")
        else:
            print("",end="")
    print()
'''
