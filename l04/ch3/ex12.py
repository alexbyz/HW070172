#exercise 12
#quadratic sum


def main():
    print("this programm calculates sum up to a given number\n")

    n = int(input("enter a number to sum up to "))    

    sum = (n*(n+1)*(2*n+1)/6)

    print("the sum is ", sum)

    input("Press a key to end the programm")
main()