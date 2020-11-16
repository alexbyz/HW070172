def main():

    filename = input("infile: ")
    infile = open(filename, "r")
    outfilename = input("outfile: ")
    outfile = open(outfilename, "w")

    for line in infile:
        inString = line.split()
        line = ""

        for i in range(len(inString)):            
            if len(inString[i]) == 4:
                line = line +" "+ "****"
                
            else:
                line = line + " " + inString[i]
                
        print(line, file=outfile)

    infile.close()
    outfile.close()        

main()