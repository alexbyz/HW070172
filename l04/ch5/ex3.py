#ex 2 ch 5
#score

def main():
    inScore = input("Enter a score [1-100 points]: ")

    scores = []
    for i in range(0,60):
        scores.append("F")
    for i in range(60,70):
        scores.append("D")
    for i in range(70,80):
        scores.append("C")
    for i in range(80,90):
        scores.append("B")
    for i in range(90,101):
        scores.append("A")

    g = scores[int(inScore)]

    print("the grade is: {0}".format(g))

main()