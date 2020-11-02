#ex 2 ch 5
#score

def main():
    inScore = input("Enter a score [1-5points]: ")

    scores = ["F", "F", "D", "C", "B", "A"]
    s = scores[int(inScore)]

    print("the grade is: {0}".format(s))

main()