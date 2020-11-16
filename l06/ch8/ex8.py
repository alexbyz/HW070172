def main():
    n , m = eval(input("enter two number (n1,n2) "))
    n1 = n
    n2 = m

    while m > 0:
        n, m = m, n%m

    print("GCD of {0} and {1} is {2}".format(n1,n2,n))


main()