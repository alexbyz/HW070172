#exercise 1
#Alexander Huber
#volume and surface of a sphere
# V = 4/3pi*r^2
# A = 4pi * r^2
# (unit) as it does not matter for the programm if its in cm, inches or some fantasy-unit

import math

def main():
    print("calculates the Surface Area and the Volume of a Sphere\n")
    rad = float(input("what is the radius? "))
    vol = 4/3 * math.pi * rad**3
    sur = 4 * math.pi * rad**2

    print("The surface of a sphere with a radius of ",rad, "(unit) is ", sur, "(unit^2), the volume is", vol, "(unit^3)\n")
    input("Press a key to end the programm")

main()

