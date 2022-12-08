class solution:
    def decode(self,s:str)->str:
        st=[]
        ts=[]
        i=0
        while i<len(s):
            if s[i].isdigit():
                res=i
                while s[res].isdigit():res=res+1
                ts.append(s[i:res])
                ts.append(st)
                i=res
                st=[]
            elif s[i]==']':
                st=ts.pop()+int(ts.pop())*st
            else:
                st.append(s[i])
        return ''.join(st)  
def main():
    n=input()
    s=solution()
    output=s.decode(n)
    print(output)
main()                          

