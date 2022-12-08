#basic 
list=[43,56,67,89,93]
print(list)
#for print the index 
print(list[-1])
print(list[2])

# print number from 3rd element
print(list[2:])
# by using negative element
print(list[-3:])

#adding another list
names=["Dhiraj","bunny","Rahul","Kundan","Dhoni"]
print(names)
list1=[list,names]
print(list1)
# adding in the last of list
list.append(98)
print(list)
# insert in between of the list
list.insert(3,76)
print(list)
#want to remove element from list
list.remove(43)
print(list)
# want to delete using index number
list.pop(0)
print(list)
# want to delete last element of list
list.pop()
print(list)
# want to delete specific element from list
del list[2:3]
print(list)
# add multiple elements in list
list.extend([32,43,54,65])
print(list)
#  find minimum
print(min(list))
# find maximum in list
print(max(list))
#sum of list
print(sum(list))
# want sort the number in ascending order
list.sort()
print(list)