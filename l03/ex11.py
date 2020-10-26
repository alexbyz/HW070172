#ex11.py
#universal converter
#by Alexander Huber
#exercises 11

def main():
    print("This programm converts a given number by an entered modifier\n")
    print("examples:\ninches to cm: 2.54\ncm to inches: 0.39\npounds to kg: 0.453\n")
    multip = eval(input("enter modifier\t"))
    valueA = eval(input("First Value "))
    valueB = valueA * multip
    print(valueA,"*", multip,"=", valueB)
    input("press any key to end the program\n")
main()

