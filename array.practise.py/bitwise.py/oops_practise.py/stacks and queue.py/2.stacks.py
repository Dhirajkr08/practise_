class solution:
    def havels(self,s:str)->bool:
        vowels=(['a','e','i','o','u','A','E','I','O','U'])
        i=0
        j=len(s)//2
        while j<len(s):
            if s[i] in vowels:
                count=count+1
            elif s[j] in vowels:
                count=count-1
            i=i+1
            j=j+1
        return count==0
def main():
    n=input()
    s=solution()
    output=s.havels(n)
    if output:
        print(True)
    else:
        print(False)
main()                    
