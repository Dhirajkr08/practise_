"""
s={"geeks","for","geeks"}
print(type(s))
print(id(s))

"""

# when we use (set ) it is mutable
"""myset=set(["a","b","c","d"])
print(myset)
myset.add("e")
print(myset)"""

# when we use frozen set it is mutable 
"""
c=frozenset(["a","b","c"])
print(c)
# normal set
c=set(["hello","world"])
print(c)
c.add("endavors")
print(c)
"""
'''
# frozen set
n=frozenset({"hello","world"})
print(n)
n.add("HOw")
print(n)'''

"""
people ={"Bunny","dhiraj","amit"}
print("people: ",end=" ")
print(people)
people.add("Harsh")
print(people)
for i in range(1,6):
    people.add(i)
print("set after the element",end=" ")
print(people)
""" 

#using union operator:
"""people={"jay","idrish","archii"}
vampires={"karan","arjun"}
dracula={"johnny","sins"}
s=people.union(vampires)
print(s)"""

#using union by "|" operator:
"""
people={"jay","idrish","archii"}
vampires={"karan","arjun"}
dracula={"johnny","sins"}

p=people|vampires|dracula
print("union using  this '|'  operator:",end=" ")
print(p)
"""

# intersection() opertor
'''set1=set()
set2=set()
for i in range(5):
    set1.add(i)
for i in range(3,10):
    set2.add(i)
set3=set1.intersection(set2)
print("intersecting using intersection() function:")
print(set3) '''


'''
# difference() operator
se1=set()
se2=set()
for i in range(5):
    se1.add(i)
for i in range(3,9):
    se2.add(i)
se3=se1.difference(se2)    
print("difference of two sets using difference () fun.:")
print(se3) 
se3=se1-se2
print("difference of two sets using '-' operator:") 
print(se3) ''' 


# usining clear method
'''
s={1,2,3,4,5}
print(s)
s.clear()
print(s)
'''

'''set1=set()
set2=set()
for i in range(1,6):
    set1.add(i)
for i in range(3,8):
    set2.add(i)
print("set1=",set1)
print("set2=",set2)
set3=set1|set2
print("uniom of set1&set2 is: set3=",set3)
set4=set1 & set2
print("intersection of set1 and set2 is set4=",set4)
if set3>set4:
    print("set3 is superset of s4")
elif set3<set4:
        print("set3 is subset of set4")
else:
    if set3==set4:
        print("set3 is same as set4") 
if set4<set3 :
    print("set4 is subset of set3")
elif set4>set3:
    print("set4 is superset of set3")
else:
    if set4==set3:
        print("Both are same")
s5=set3-set4
print("element is set3 and not in set4 is:",s5)
if set4.isdisjoint(s5):
    print("nothing in common")
s5.clear()
print("after clearing s5:",s5)    
            


