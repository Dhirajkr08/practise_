def find_distance(distance):
    
    if distance>=1000:
        print(12)
            

    elif distance>500 and distance <1000:
        print(10)
            

    elif distance >100 and distance<=500:
        print(8)
            

    elif distance<=100:
        print(5)
            
    else:
        print("invalid")
def main():
    distance=int(input())
    find_distance(distance)
main()                               