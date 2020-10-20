#exercise 5
def main():

    print("Chaotic Function")
    x = eval(input("Number between 0 and 1:\n"))
    n = eval(input("How many lines?:\n"))
    for i in range(n):
        x = 2.0 * x * (1-x)
        print(i+1,". =",x)

main()
