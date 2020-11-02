#ex 13 ch 5
#batch oriented

def main():

    print("Chaotic Function")

    inFileN = input("Filename input? ")
    outFileN = input("Filename output? ")

    infile = open(inFileN, "r")
    outfile = open(outFileN, "w")

    for line in infile:
        x1, x2, n = line.split()

    x1 = float(x1)
    x2 = float(x2)
    n = int(n)

    print("\n{0:^5} {1:^7.5} {2:^7.5}".format("index", x1, x2), file=outfile)
    print("---------------------", file=outfile)

    for i in range(n):
        x1 = 3. * x1 * (1-x1)
        x2 = 3.9 * x2 * (1-x2)
        print("{0:^5} {1:>7.5f} {2:>7.5f}".format((i+1), x1, x2), file=outfile)

    infile.close()
    outfile.close()
main()