#exercise 1
def main():

    print("Chaotic Function")
    x1 = eval(input("Number between 0 and 1 for the first column:\n"))
    x2 = eval(input("Number between 0 and 1 for the second column:\n"))
    n = eval(input("How many lines?:\n"))
    for i in range(n):
        x1 = 2.0 * x1 * (1-x1)
        x2 = 2.0 * x1 * (1-x2)
        print(i+1,".=",x1, "\t" , x2)

main()
