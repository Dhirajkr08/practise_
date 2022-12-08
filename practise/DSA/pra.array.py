#using array with for loop
'''
from array import *
vals=array('b',[1,4,6,7,9,3])
newarr=array(vals.typecode,(a*a for a in vals))
for r in newarr:
    print(r)
'''

'''
from array import *
value=array("b",[21,35,62,79])
newv=array(value.typecode,(a for a in value))
i=0
while i<len(newv):
    print(newv[i])
    i=i+1
'''

'''
from array import *
vals=array("b",[12,34,56,32,67])
new_vals=array(vals.typecode,(a for a in vals))
i=0
while i<len(new_vals):
    print(new_vals[i])
    i=i+1
'''

# print list
"""list=["bunny",12,"dhiraj",24]
print(list)"""

"""def find_maximum(arr, length):
    max=arr[0]
    for i in range(0,len(arr)):
        
        if (arr[i]>max):
            max=arr[i]
    return max        
    


def main():
    n = int(input())
    arr=[]
    for i in range(n):
        arr.append(int(input()))
    print(find_maximum(arr, n))
    
main()
"""

def find_maximum(arr,length):
    max=arr[0]
    for i in range(0,len(arr)):
        if (arr[i]>max):
            max=arr[i]
    return max
def main():
    n=int(input())
    arr=[]
    for i in range(n):
        arr.append(int(input()))
    print(find_maximum(arr,n))    
    