"""dict={}
print("Empty dictonay:")
print(dict)
# adding elements
dict[0]="geeks"
dict[1]="for"
dict[2]=1
print("dictionary after 3 elements:")
print(dict)
## adding set of value to single key:
dict["value_set"]=2,3,4
print("dictionary after 3 elements:")
print(dict)
# update existing key value
dict[2]="welcome"
print("updating key value:")
print(dict)
#adding nested key value
dict[5]={'nested':{"1":"life","2":"geeks"}}
print("adding nested key:")
print(dict)
"""

"""
#createing a dictionary
dict={1:"geeks","name":"for","bunny":"Geeks"}
print("Accessing the element using key:")
print(dict["name"])
print(dict["bunny"])
print(dict[1])
"""

"""
# create dictionary
dict={1:"geeks","two":"for",3:"geeks"}
print("accessing the element using get:")
print(dict.get("two"))
"""

#create the dictionary and accessing the nested dictionary
'''
dict={'dict1':{1:"geeks"},'dict2':{"two":"for"}}
print("accessing the nested elements:")
print(dict['dict1'])
print(dict['dict1'][1])
print(dict['dict2']["two"])
'''

"""
dict={1:"python",2:"is",3:"fine",4:"like",5:"wine"}
dict1=dict.copy()
print(dict1)
dict1.clear()
print(dict1)
print(dict.get(2))
print(dict.items())
print(dict.keys())
print(dict.pop(2))
print(dict)
dict.popitem()
print(dict)
dict.update({2:"always"})
print(dict)
print(dict.values())
"""

