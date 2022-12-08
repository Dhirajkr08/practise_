class solution:
    def decode_string(self,s:str)->str:
        st=[]
        ts=[]
        i=0
        while i<len(s):
            if s[i].isdigit():
                run=i
                while s[run].isdigit():run=run+1
                ts.append(s[i:run])
                ts.append(st)
                st=[]
                i=run
            elif s[i]==']':
                st=ts.pop()+int(ts.pop())*st
            else:
                st.append(s[i])
            i+=1
        return ''.join(st)
def main():
    n=input()
    s=solution()
    output=s.decode_string(n)
    print(output)
main()                



                      

        
  
