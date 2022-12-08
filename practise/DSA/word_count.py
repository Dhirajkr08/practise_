string=input()
word=str(input())
count=0
for i in string:
    if i ==word:
        count=count+1
print(word,count)        