#ex2

def main():
    score = int(input("enter a score"))

    if score == 0 or score == 1:
        print("F")
    elif score == 2:
        print("D")
    elif score == 3:
        print("C")
    elif score == 4:
        print("B")
    elif score == 5:
        print("A")
    else:
        print("The professor forgot how many points could be achieved")

main()