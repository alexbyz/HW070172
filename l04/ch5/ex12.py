#ex 12 ch 5
#futval

def main():
    print("this programm calculates future values of an investment\n")
    principal = eval(input("Enter the initial Value:\t"))
    initial = principal

    apr = float(input("\nEnter the annual interest rate (in %):\t")) / 100   

    dur = int(input("\nfor how many years should interest be calculated?:\t"))

    yearlyDep = float(input("\nDo you have a yearly deposit?:\t"))    

    print("\n{0:^5} {1:^5}".format("year", "value"))
    print("-------------")

    for i in range(dur):
        principal = (principal * (1 + apr )) + yearlyDep
        print("{0:^5} {1:>7.2f}".format((i+1), principal))    
    
    input("press any key to end the program\n")

main()