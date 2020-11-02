#ex 4 ch 5
#acronyme

def main():
    print("This programm creates an acronyme\n")
    inString = input("enter a Phrase\n")
    ac = []

    for string in inString.split(): #splits the phrase
        first = string[0].upper()   #takes the fist entry as a upper case char
        ac.append(first)            #appends it to a list
    print("".join(ac))              #prints a string again

main()