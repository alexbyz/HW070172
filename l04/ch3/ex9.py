#exercise 9
#area triangle

def main():
    print("this programm calculates the area of a triangle from its sides\n")
    a = float(input("first side "))
    b = float(input("second side "))
    c = float(input("thired side "))

    s = (a+b+c)/2
    arr = (s*(s-a)*(s-b)*(s-c))**0.5

    print("The area is ",arr)

    input("Press a key to end the programm")
main()