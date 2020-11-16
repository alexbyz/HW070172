def main():

    x = int(input("enter a positive whole number > 2: "))
    if x < 2:
        print("negative number or < 2")
    else:
        i = 2
        sqroot = x**0.5

        while i <= sqroot:
            if x % i != 0:
                i = i+1
            else:
                print("not prime")
                quit()
        print("prime")


main()