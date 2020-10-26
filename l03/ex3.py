#ex3.py
#average of 3 scores
#by Alexander Huber
#exercise 3

def main():
    print("This programm calculates the average of 3 input values")
    sc1, sc2, sc3 = eval(input("Please enter 3 values, seperate by ,\n"))
    av = (sc1 + sc2 + sc3) /3
    print ("the average of",sc1,",",sc2,", and",sc3," is: ", av)
    input("press any key to end the program\n")
main()