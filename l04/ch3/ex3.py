#exercise 3
#molecular weight of carbohydrate

def main():
    print("this programm calculates the monlecular weight of a carbohydrate molecule (g/mol)\n")
    h = int(input("how many atoms of hydrogen? "))
    c = int(input("and carbon? "))
    o = int(input("and finally oxygen? "))

    mw = h * 1.00794 + c * 12.0107 + o * 15.9994

    print("a molecule with ",h," hydrogene, ",c," carbon and ",o," oxygen atoms weighs ",mw, "g/mol")
    
    input("Press a key to end the programm")
main()