#ex3

def main():
    score = int(input("enter a score"))

    if score < 60:
        print("F")
    elif score <=69:
        print("D")
    elif score <=79:
        print("C")
    elif score <=89:
        print("B")
    elif score <=100:
        print("A")
    else:
        print("The professor forgot how many points could be achieved")

main()