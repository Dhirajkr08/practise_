# for finding weather it is set or dictioanry 
'''var={"geeks","for","geeks"}
print(type(var))
'''
# set () for typecasting 
'''
m=set(["hello","mini","world"])
print(m)
'''

# adding element to set
'''m.add("cute")
print(m)'''


# frozen set
# frozen set is immutable
'''frozen_set=frozenset(["a","b","c","d","f"])
print(frozen_set)
frozen_set.add("h")
print(frozen_set)
'''

# creating a set
'''p={"ram","sita","Hanuman","laxman"}
print(p)
#adding people in p
p.add("Bharath")
print(p)
for i in range(1,8):
    p.add(i)
print(p)  
'''
# union of two sets
'''people={"bunny","dhiraj"}
god={"ganesha","krishna","Makhanchor","radhekrishna"}
mahadev={"shiva","tandav","shambhu"}
#union using union()
om=god.union(mahadev)
print(om)'''
# union using | operator
'''om=god|mahadev
print(om)'''

#demonstrate intersection of two sets
'''set1=set()
set2=set()
for i in range(1,5):
    set1.add(i)
for i in range(2,9):
    set2.add(i)'''
#using intersection operator
'''set3=set1.intersection(set2)
print(set3) ''' 

# intersection using & operator
'''set3=set1&set2
print(set3)'''

# using difference operator
'''set1=set()
set2=set()
for i in range(5):
    set1.add(i)
for i in range(2,9):
    set2.add(i)'''
# using difference() operator    
'''set3=set1.difference(set2)
print(set3)'''  
# using '-' operator for difference
'''set3=set1-set2
print(set3) '''

# creating a set
'''s={'a','b','c','d','e','f','g'}
print(s)
s.clear()
print(s)'''

# demonstrate working # of set python
set1=set()
set2=set()
# adding element to set1
for i in range(1,6):
    set1.add(i)
# adding element to set2
for i in range(3,8):
    set2.add(i)
print(set1)
print(set2) 

# union of set1 and set2
set3=set1|set2
print(set3)
# intersection of set1 and set2
set4=set1&set2
print(set4)
# check relational between set3 and set4
if set3>set4:
    print("set3 is superset of set4")
elif set3<set4:
    print("set3 is subset of set4")
else:
    print("set3 is same as set4")
# check difference
set5=set3-set4  
print(set5) 
if set4.isdisjoint(set5):
    print("set4 and set5 nothing have common") 

  

