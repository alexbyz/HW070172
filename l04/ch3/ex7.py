#exercise 7
#distance of two points in a plane

def main():
    print("this programm calculetes the distance between two points \n")
    x1, y1 = eval(input("enter the x and y coordinate of the first point (x1,y1)"))
    x2, y2 = eval(input("enter the x and y coordinate of the second point (x2,y2)"))

    dist = ((x2-x1)**2 +(y2-y1)**2)**0.5

    print("the distance is ", dist)

    input("Press a key to end the programm")
main()