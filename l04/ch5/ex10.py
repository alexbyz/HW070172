#ex 10 ch 5
#word counter

def main():
    print("This programm counts words in a sentence\n")
    sent = (input("enter a stentence\n"))

    sum = 0
    i = 0

    for string in sent.split():        
        sum = sum + len(string)        
        i = i+1
        avg = sum / i 

    print(avg)
main()