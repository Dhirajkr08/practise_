def convertBinary(num):
    binaryArray = []
    while num>0:
        binaryArray.append(num%2)
        num = num//2
    for j in binaryArray:
        print(j, end="")

def main():
    decimal_num =int(input())
    convertBinary(decimal_num)
main()    