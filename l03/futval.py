#futval.py
#future investments
#by Alexander Huber
#ex6, ex7, ex8

def main():
    print("this programm calculates future values of an investment\n")
    principal = eval(input("Enter the initial Value:\t"))
    initial = principal

    apr = eval(input("\nEnter the annual interest rate (in %):\t")) / 100   
    
    periode = eval(input("\nHow often per year should interest be calculated?:\t"))

    dur = eval(input("\nfor how many years should interest be calculated?:\t"))

    yearlyDep = eval(input("\nDo you have a yearly deposit?:\t"))    

    for i in range(dur * periode):
        principal = (principal * (1 + (apr / periode))) + yearlyDep
    print("in", dur,"years the initial value of", initial, "will have grown to: ", principal, "at a rate of",apr*100,"% with interest added", periode,"times a year")
    input("press any key to end the program\n")
main()

