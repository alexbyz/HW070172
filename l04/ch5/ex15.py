#ex 14 ch 5
#batch oriented

def main():    

    inFileN = input("Filename input? ")

    infile = open(inFileN, "r")

    lineC = 0
    wordC = 0
    charC = 0

    for line in infile:     
        lineC = lineC + 1    #counts lines

        words = 0
        chs = 0
        for string in line.split():        
            words = words+1     #counts words in a line
            chs = chs + len(string)
        wordC = wordC + words        #sums up the words
        charC = charC + chs          #sums up the characters 

    print(lineC, wordC, charC)
    infile.close()
main()