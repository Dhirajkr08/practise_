def get_bit(n,i):
    return((n &(1<<i))!=0)
def set_bit(n,i) :
    return n|(1<<i) 
def clear_bit(n,i):
    m=~(1<<i)
    return n & m
n=70
print (1 if (get_bit(n,3))else "0" )
print(set_bit(n,0))
print(clear_bit(n,0))        