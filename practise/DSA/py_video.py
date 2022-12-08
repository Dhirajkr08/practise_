class solution:
    def isvalid(self,string):
        open_stack=[]
        open_brace=["(","[","{"]
        close_brace=[")","]","}"]
        Flag=True
        for i in range(int(string)):
            if string[i] in close_brace:
                if len(open_stack)==0:
                    flag=False
                    break
                else:
                    c=open_brace[close_brace.index(string[i])]
                    if c==open_stack[-1]:
                        open_stack.pop()
                        flag =True
                        continue
                    else:
                        flag=False
                        break
            elif string[i] in open_brace[close_brace.index(string[i])] :
                open_stack.append(string[i])
        if len (open_stack)>0:
            flag=False
        return flag


