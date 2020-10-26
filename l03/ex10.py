#ex10.py
#miles to km
#by Alexander Huber
#exercises 10

def main():
    print("this programm converts a distance in miles to a sensible unit")
    distM = eval(input("A distance in miles "))
    distKm = distM * 1.609 
    print(distM,"miles are ", distKm,"km")
    input("press any key to end the program\n")
main()

