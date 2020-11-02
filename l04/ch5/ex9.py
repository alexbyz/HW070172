#ex 9 ch 5
#word counter

def main():
    print("This programm counts words in a sentence\n")
    sent = (input("enter a stentence\n"))

    i = 0

    for string in sent.split():        
        i = i+1

    print(i)

main()