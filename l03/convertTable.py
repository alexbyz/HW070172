#convert.py
#prints °C and °F from 0 to 100°C all 10°septs
#by Alexander Huber
#ex5

def main():
    print("this programm prints temp from 0°C to 100°C in 10° septs")
    for i in range(11):
        tempCe = i * 10
        tempFa = tempCe * 9/5 +32
        print(tempFa,"°F equals to: ", tempCe,"°C")
    input("press any key to end the program\n")
    
main()