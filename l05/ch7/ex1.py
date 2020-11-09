#ex1

def main():
    hours = int(input("enter the number of hours worked "))
    hRate = 10

    if hours > 40:
        wage = 40 * hRate + (hours - 40)* hRate * 1.5
    else:
        wage = hours * hRate
    
    print("the wage is ", wage)

main()