#exercise 5
#cost of order

import math

def main():
    print("this programm calculates the cost of an order\n")

    mass = float(input("how much coffee was bought (in pounds)? "))

    cost = mass * 10.5 +  math.ceil(mass) * 0.86 + 1.5 #so that they have to pay for the next whole pound too

    print("the order cost ",cost,"including shipping")
    
    input("Press a key to end the programm")
main()