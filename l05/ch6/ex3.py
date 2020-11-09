#ex3
#spere Area and volume

import math

def sphereArea(radius):
    return 4 * math.pi * radius**2

def sphereVolume(radius):
    return 4 * math.pi * radius**3 / 3

def main():
    print("This programm calculates the Surface Area and the Volume of a sphere\n")
    radius = float(input("enter the radius "))
    print("The surface Area is {0:10.3f} and the Volume is {1:10.3f}".format(sphereArea(radius), sphereVolume(radius)))

main()