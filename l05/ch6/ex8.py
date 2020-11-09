#exercise 8
#pi roots guess and check

import math

def guess(score, x):
    g = score /2
    for i in range(x):        
        g = (g + (score/g)) / 2
    return g

def main():
    print("this programm calculates a sqrroot by guess and check approximation\n")
    
    q = abs(float(input("enter a number\n"))) #no negative number please
    n = int(input("how many guesses? "))    
    
    print("the approximated result is ", guess(q,n))
            
    input("Press a key to end the programm")
main()