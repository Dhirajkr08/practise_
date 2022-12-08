class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class stack:
    def __init__(self):
        self.head=Node("head")
        self.size=0
    def __str__(self):
        cur=self.head.next
        out=""
        while cur:
            out=out+str(cur.value)+"->" 
            cur=cur.next
        return out[::-3]
                      