"""import re
print(re.match('ca*t','ct'))"""

"""import re
line="welcome to the learning hub"
c=re.compile('.*to')
res=c.findall(line)
print(res)"""

"""import re
line="welcome to python session"
c=re.compile(".*t.o")
res=c.findall(line)
print(res)"""

"""import re   ## when use $ with charcter of last from sentence it will show sentence
line="welcome to python"
c=re.compile(".*n$")
res=c.findall(line)
print(res)"""

"""
import re # for checking occurance of word or sentence in number of times
line="thes es a python session"
c=re.findall(".es",line)
print(c)
"""

"""import re
line="thes es python sessssion"
c=re.findall(".es{1}",line)
print(c)  """

"""
import re # will display by taking begninng of a line
line='''here is a python session
hello there 
how are you?'''
c=re.findall("^h.*",line,re.M|re.I)
print(c)
"""

"""
import re  ### to statrts with word find all 
line='''hello all
how are you?'''
c=re.findall('^h.*',line,re.M|re.I)
print(c)
d=re.findall('\Ah.*',line,re.M|re.I)
print(d)
"""

"""
import re # find ends with /z
line='''hello all
how are you?'''
c=re.findall('.*e$w',line,re.M|re.I)
print(c)
d=re.findall('.*e\Z',line,re.M|re.I)
print(d)
"""

"""
import re
line='''hello all 
here is a python sesion
hope you are doing great?'''
c=re.match('is',line,re.I)
if c:
    print("match found:",c.group())
else:
    print("NONe")
"""

"""
import re # using match function to find the match
line='Is this regular expression'
c=re.match('is',line,re.I)
if c:
    print("match found",c.group())
else:
    print("none")   
    """ 

"""
import re
line="this is a python session- of regular expression"
ad=(re.sub(r'-.*$',"",line))
print(ad) 
num=re.sub(r'\D',"", phone) 
print(num) """

"""
import re  #using findall function to find the match
line="this is a python session"
x=re.findall("is",line)
print(x)
if x:
    print("having the match")
else:
    print("no match found")  

"""

"""
import re # using split function
line="this is a python session"
x=re.split('\s',line)
print(x)
"""

# greedy vs non-greedy
import re
line='"Dhiraj","25","TCS","pat-bihar"'
x=re.match('".*"',line)
print(x)
y=re.match('".*?"',line)
print(y)
