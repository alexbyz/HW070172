#exercise 10
#ladder

import math

def main():
    print("this programm calculates the required lenght of a ladder\n")
    height = float(input("how high is the obsacle (in m)? "))
    ang = float(input("what should be the angle of the ladder (in °) "))

    angrad = (math.pi * ang)/ 180

    ladder = height / math.sin(angrad)

    print("The ladder has to be ",ladder, "m long")

    input("Press a key to end the programm")
main()