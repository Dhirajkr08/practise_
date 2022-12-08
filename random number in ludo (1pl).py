import random
from timeit import repeat
repeat = True
while repeat:
    print("you rolled",random.randint(1,6))
    print("do you want to roll again? Y/N")
    repeat = "y" in input()