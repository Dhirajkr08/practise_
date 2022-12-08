"""def find_prime(n):
    for i in range(2,n+1):
        if i>1:
            for j in range(2,i):
                if(i%j)==0:
                    break
            else:
                print(i)    
def main():
    n=int(input())
    find_prime(n)
main()    
"""
def count_prime(self,n):
    count=0
    prime=[False for i in range(n+1)]
    for i in range(2,n):
        if prime[i]==False:
            count=count+1
            j=2
            while j*i<n:
                prime[j*i]=True
                j=j+1
    return count            
