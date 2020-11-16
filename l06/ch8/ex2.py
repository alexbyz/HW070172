#again?

def chill(v,t):
    windC = 35.74 + 0.6215*t - 35.75*v**0.16 + 0.4275*t*v**0.16
    if v > 3:
        return windC
    else:
        return 0.0

def main():

    print("temp °F: {0:<7} {1:<7} {2:<7} {3:<7} {4:<7} {5:<7} {6:<7} {7:<7}".format(-20, -10, 0, 10, 20, 30, 40, 50))
    for v in range (0,55,5):    
        printW = "         "
        for t in range (-20,60,10):
            c = chill(v,t)
            printW = printW + "{0:<4.2f}".format(c) + "\t"
        print(printW)    

main()