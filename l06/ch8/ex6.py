def checkPrime(x):
    i = 2
    sqroot = x**0.5

    while i <= sqroot:
        if x % i != 0:
            i = i+1
        else:
            return False
        return True


def main():

    n = int(input("enter a number "))

    if n < 2:
        n = 2

    for i in range(n):
        if checkPrime(i) == True:
            print(i)

main()