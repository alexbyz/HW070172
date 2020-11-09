#ex5
#cost per square unit of a pice, given radius and price

import math

def a(radius):
    return math.pi * radius**2

def cPerA(radius, price):
    return a(radius) / price

def main():
    print("cost per square unit of a pice, given radius and price")
    rad = float(input("How big is the pizza? (enter radius)\n "))
    price = float(input("and how much does it cost? "))

    print("the pizza costs ", cPerA(rad, price)) 

    input("Press a key to end the programm")
main()