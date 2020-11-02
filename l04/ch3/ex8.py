#exercise 8
#epact gregorian calender

def main():
    print("this programm does what late antique bishops quarrel over")

    year = int(input("enter a year (4 digits)"))
    c = year // 100
    epact = (8+(c//4) - c + ((8*c+13)//25)) + (11 * (year%19))%30

    print("the epact of ",year,"is ",epact)

    input("Press a key to end the programm")
main()