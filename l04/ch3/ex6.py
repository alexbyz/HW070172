#exercise 6
#slope of two points in a plane

def main():
    print("this programm calculetes the slope between a line (non vertical!)\n")
    x1, y1 = eval(input("enter the x and y coordinate of the first point (x1,y1)"))
    x2, y2 = eval(input("enter the x and y coordinate of the second point (x2,y2)"))

    sl = y2-y1 / x2-x1
    print("the slope is ", sl)
    
    input("Press a key to end the programm")
main()