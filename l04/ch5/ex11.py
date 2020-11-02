#ex 11 ch 5
#chaotic formated

def main():

    print("Chaotic Function")
    x1 = float(input("Number between 0 and 1 for the first column:\n"))
    x2 = float(input("Number between 0 and 1 for the second column:\n"))
    n = int(input("How many lines?:"))

    print("\n{0:^5} {1:^7.5} {2:^7.5}".format("index", x1, x2))
    print("---------------------")

    for i in range(n):
        x1 = 3. * x1 * (1-x1)
        x2 = 3.9 * x2 * (1-x2)
        print("{0:^5} {1:>7.5f} {2:>7.5f}".format((i+1), x1, x2))
main()