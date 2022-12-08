'''Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated 
exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed,etc. 
Furthermore,you may assume that the original data does not contain any digits and that digits are only for those repeat numbers,
k. For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 105.

 '''

class solution:
    def decodeString(self,s:str)->str:
        st=[]
        ts=[]
        i=0
        while i<len(s):
            if s[i].isdigit():
                res=i
                while s[res].isdigit():res=res+1
                ts.append(s[i:res])
                ts.append(st)
                st=[]
                i=res
            elif s[i]==']':
                st=ts.pop()+int(ts.pop())*st
            else:
                st.append(s[i])
            i=i+1
        return ''.join(st)
def main():
    n=input()
    s=solution()
    output=s.decodeString(n)
    print(output)
main()                            
