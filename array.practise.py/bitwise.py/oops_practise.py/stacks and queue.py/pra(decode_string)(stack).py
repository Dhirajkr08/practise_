class solution:
    def decode(self,s:str)->str:
        i=0
        st=[]
        ts=[]
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
    n="2[abc]3[cd]ef"
    s=solution()
    output=s.decode(n)
    print(output)
main()                

