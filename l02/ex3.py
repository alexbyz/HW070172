#exercise 1
def main():

    print("Chaotic Function")
    x = eval(input("Number between 0 and 1:\n"))
    for i in range(10):
        x = 2.0 * x * (1-x)
        print(x)

main()
