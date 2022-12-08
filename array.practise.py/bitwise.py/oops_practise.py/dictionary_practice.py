"""dict={1:"hello",2:"for",3:"HEllo"}
print(dict) 
"""
# crreating the mixed keys:
"""dict={1:[1,2,3,4,5],"names":["geeks for geeks"]}
print(dict)
"""
# create a dictionary for user input
"""def create_dic(n):
    employee={}
    for i in range(n):
        key=int(input("key="))
        value=str(input("VAlue ="))
        employee[key]=value
    print( employee)
def main():
    n=int(input()) 
    create_dic(n) 
main() 
"""

# creating a dictionary
# with each item as a pair
'''Dict=dict([(1,"geeks"),(2,"geeks")])
print(Dict)
'''


'''dic=dict([(1,"john"),(2,"Dhiraj"),(3,"Rahul")])
print(dic)
'''

# creating a nested dictionary
'''
Dict={1:'Geeks',2:'for',3:{"a":'welcome',"b":'to',"c":'hell'}}
print(Dict)
'''


#creating empty dictionary:
'''Dict={}
print("Empty Dictionary:")
print(Dict)'''

# adding elements one at a time
'''Dict[0]="geeks"
Dict[1]="For"
Dict[2]=1
print(Dict)'''

# adding set of values
# to a single key
'''Dict['Value_Set']=2,3,4
print(Dict)'''

#update key value
'''Dict[2]="Geeks"
print(Dict)'''

#Adding Nested key value to dictionary
'''Dict[4]={'key':{1:'Life',2:'hack'}}
print(Dict)'''

# accessing a element using key
'''
Dict={1:"geeks","names":'for',3:"geeks"}
print(Dict["names"])
print(Dict[1])
'''


# we can use get () method accessing the element
'''
Dict={1:"geeks","names":'for',3:"geeks"}
print(Dict.get(3))
'''

#accessing the element from nested Dictionary
'''
Dict={'Dict1':{1:'Geeks'},'Dict2':{2:"Hello"}}
print(Dict['Dict1'])
print(Dict['Dict1'][1])
'''

'''Dictionary methods
* clear() – Remove all the elements from the dictionary
* copy() – Returns a copy of the dictionary
* get() – Returns the value of specified key
* items() – Returns a list containing a tuple for each key value pair
* keys() – Returns a list containing dictionary’s keys
* pop() – Remove the element with specified key
* popitem() – Removes the last inserted key-value pair
* update() – Updates dictionary with specified key-value pairs
* values() – Returns a list of all the values of dictionary'''

# demo for all dictionary methods
dict1={1:"hello",2:"python",3:"how",4:"you"}
# copy() method
dict2=dict1.copy()
print(dict2)

#clear() method
dict1.clear()
print(dict1)

#get() method
print(dict2.get(1))

#items() method
print(dict2.items())

#keys() method
print(dict2.keys())

#pop() method
dict2.pop(2)
print(dict2)

# popitem() method
dict2.popitem()
print(dict2)

# update() method
dict2.update({3:'Python'})
print(dict2)

# values() method
print(dict2.values())