#ex4

def sumN(n):
    return (n**2 + n) / 2

def sumNCubes(n):
    return (n*(n+1)*(2*n+1)/6)

def main():
    n = float(input("Number to sum up to "))
    print("The sum up to {0} is {1:10.3f} and the quadratic sum is {2:10.3f}".format(n, sumN(n), sumNCubes(n)))

main()