'''a=[1,2,3,4,3,2,5,1,5,6]
xor=0
for i in a:
    xor=xor^a[i]
print(xor)
'''



'''while(n):
            count=count+1
            n=n & (n-1)
        return count '''
class solution:
    def binary_representation(self,n:int)-> bool:
        for i in range(1,len(n)):
            if n[i-1]==n[i]:
                return False
        return True
def main():
    n=int(input())
    s=solution()
    output=s.binary_representation(n)
    if output:
        print("true")
    else:
        print("false")    
main()        




