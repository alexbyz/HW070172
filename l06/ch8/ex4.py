def main():

    x = int(input("starting value: "))

    print(x)

    while x != 1:
        if x % 2 == 0:
            x = int(x / 2)
            print (x)
        else:
            x = int(3*x+1)
            print (x)


main()