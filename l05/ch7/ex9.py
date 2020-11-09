#ex9

def easter(year):
    a = year % 19
    b = year % 4
    c = year % 7
    d = (19*a+24)%30
    e = (2*b+4*c+6*d+5)%7

    return 22+ d + e

def main():
    year = int(input("enter a year between 1982-2048 "))

    if year <= 1982 or year >= 2048:
        print("the year is not within the range")
    else:
        date = easter(year)
        if date <= 31:
            print("easter is on the {0}.March {1}".format(date, year))
        else:
            print("easter is on the {0}.April {1}".format(date-31, year))

main()