#exercise 4
#distance of lightning strike

def main():
    print("this programm calculates the distance of a lighning strike based on the time between flash and thunder\n")

    ti = float(input("time passed: "))    
    dist = 1100 * ti

    dist = dist / 5280

    print("the lightning strike was about", dist, "miles away")
    
    input("Press a key to end the programm")
main()