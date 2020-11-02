#ex 6 ch 5
#numeric value

def main():
    print("This programm calculates a numeric value for a name\n")
    name = (input("enter a Name\n")).lower()

    name = name.replace(" ", "")

    sum = 0

    for ch in name:
        sum = int(ord(ch)) + sum - 96 
    print("The names sum is ",sum)
main()