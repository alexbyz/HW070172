#exercise 2
#cost per square unit of a pice, given radius and price

import math

def main():
    print("cost per square unit of a pice, given radius and price")
    rad = float(input("How big is the pizza? (enter radius)\n "))
    price = float(input("and how much does it cost? "))

    arr = math.pi * rad**2
    cPerrArr = arr / price

    print("the pizza costs ", cPerrArr)
    input("Press a key to end the programm")
main()