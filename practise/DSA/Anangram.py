str1=input()
str2=input()
str1=str1.lower()
str2=str2.lower()
if(sorted(str1)==sorted(str2)):
    print(True)
else:
    print(False)    