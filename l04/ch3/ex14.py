#exercise 14
#finds average

def main():
    print("this programm finds the average")
    n = int(input(" fist, how many numbers do you want to enter:"))    
    sum = 0

    for i in range(n):
        sum = sum + float(input("enter a number "))    

    avg = sum / n
    print("the sum is ", avg)

    input("Press a key to end the programm")
main()