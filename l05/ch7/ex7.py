#ex7

def main():
    startH, startM = eval(input("starting hours and minutes(h,m) (24h formate)"))
    endH, endM = eval(input("starting hours and minutes(h,m) (24h formate)"))

    if startM > 60 or endM > 60 or startH > 24 or endH > 24:            
        print("wrong time")
    else:
        end = int(endH) + endM / 60    #to get a time in hours.hours
        start = int(startH) + startM / 60
        work = end - start

        if end > 21:
            end = end - 21
            bill = (work-end) * 2.5 + end * 1.75
        else:
            bill = work * 2.5
        
        print("the bill is ", bill)


main()