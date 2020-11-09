#ex6

def main():
    speed = float(input("enter the speed "))
    limit = float(input("enter the speedlimit "))

    if speed > limit:
        fine = 50 + (speed-limit)*5
        if speed > 200:
            fine = fine + 200
        print("the speedlimit was exeded by {0}mph, the fine is {1}".format((speed-limit), fine))
    else:
        print("within the speed limit")
        
main()