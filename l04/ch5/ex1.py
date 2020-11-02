#ex 1 ch 5
#dateconvert

def main():
    dateIn = input("Enter a date dd/mm/yyyy: ")
    dd, mm, yyyy = dateIn.split("/")

    months = ["Jannuary", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    mm = months[int(mm)-1]

    print("the converted date is: {0}.{1} {2}".format(dd, mm, yyyy))

main()