#ex4

def main():
    score = int(input("enter a credit score"))

    if score < 7:
        print("Freshman")
    elif score <=15:
        print("Sophomore")
    elif score <=25:
        print("Junior")
    elif score > 26:
        print("Senior")
    else:
        print("Check the entered number")

main()