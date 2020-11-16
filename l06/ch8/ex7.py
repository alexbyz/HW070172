def checkPrime(x):
    i = 2
    sqroot = x**0.5

    while i <= sqroot:
        if int(x % i) != 0:
            i = i+1
        else:
            return False
    return True

def main():

    n = int(input("enter a number "))
    x = n
    
    if n % 2 == 0:

        while x >= n/2:         #no double sums       
            if checkPrime(x) == True:   #will be false the first two times                
                n2 = n - x              #get the second part of the sum
                if checkPrime(n2) == True:  #try if the sum fits
                    print ("{0} + {1} = {2}".format(x,n2,n))
            x = x-1                     #next turn

    else:
        print("must be a positive number")
        quit

main()