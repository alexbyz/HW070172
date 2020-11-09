#ex1
#old McDoald 

def lyrics(animal):
    return oldM() + "\nAnd on that farm he had a " + animal + ei() + "\nWith a moo, moo here and a moo, moo there.\nHere a moo, there a moo, everywhere a moo, moo.\n" + oldM()

def oldM():
    return "Old MacDonald had a farm, " + ei()

def ei():
    return  " Ee-igh, Ei-igh, Oh!"

def main():
    for i in range(5):
        animal = input("Which animal?")
        print(lyrics(animal))
main()