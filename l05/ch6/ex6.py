#ex6
#area triangle

def side(a,b,c):
    return (a+b+c)/2

def ar(a, b, c):
    s = side(a,b,c)
    return (s*(s-a)*(s-b)*(s-c))**0.5

def main():
    print("this programm calculates the area of a triangle from its sides\n")
    a = float(input("first side "))
    b = float(input("second side "))
    c = float(input("thired side "))


    print("The area is ", ar(a,b,c))

    input("Press a key to end the programm")
main()