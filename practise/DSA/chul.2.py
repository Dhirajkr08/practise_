"""n=int(input())
for i in range(0,n):
    for j in range(0,i+1):
        print("*",end="")
      

    for j in range(0,i+1):
        print("*",end="")
    print()    """

"""n=int(input())
for i in range(n):
    for j in range(i+1):
        print("*",end="")
    print()
for i in range(4,n):    
    for j in range(i+1):
        print("*",end="")
    print()
    """

# pattern
'''
n=int(input())
for i in range(0,n-1):
    for j in range(i+1):
        print("*",end="")
    print() 
for i in range(0,n-1):
    for j in range(i+1):
        print("*",end="")
    print()                 
'''

"""n=int(input())
for i in range(n):
    for j in range(n-i):
        print("*",end="") 
    print()    
"""

"""n=int(input())
for i in range(n):
    for j in range(i+1):
        print("*",end="")
    print() 
"""       

n=int(input() )
i=2
while n<=i:
    print(i)
    i=i+2
