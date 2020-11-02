#exercise 17
#pi roots guess and check

import math

def main():
    print("this programm calculates a sqrroot by guess and check approximation\n")
    
    q = abs(float(input("enter a number\n"))) #no negative number please
    n = int(input("how many guesses? "))

    r = math.sqrt(q)
    guess = q /2

    for i in range(n):        
        guess = (guess + (q/guess)) / 2
    
    print("the approximated result is ",guess,"math.sqrt results to: ",r,"the difference is:", guess-r)
            
    input("Press a key to end the programm")
main()