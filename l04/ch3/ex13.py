#exercise 13
#another sum


def main():
    print("this programm calculates sums up enterd numbers,")
    n = int(input(" fist, how many numbers do you want to enter:"))    
    sum = 0

    for i in range(n):
        sum = sum + float(input("enter a number "))    

    print("the sum is ", sum)

    input("Press a key to end the programm")
main()