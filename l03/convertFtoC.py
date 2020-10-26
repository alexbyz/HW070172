#convertFtoC.py
#converts a temperature from Fahrenheit to Celsius - because other than in the textbook I cant deal with °F :)
#by Alexander Huber
#exercises 1 & 2 & 9

def main():
    print("this programm converts a Temperatur given in °F into °C")
    tempFa = eval(input("Enter a temperature in °F: "))
    tempCe = (tempFa - 32) * 5/9   
    print(tempFa,"°F equals to: ", tempCe,"°C")
    input("press any key to end the program\n")
main()

#def main():
#    print("this programm converts a Temperatur given in °C into °F")
#    tempCe = eval(input("Enter a temperature in °C: "))
#    tempFa = tempCe * 9/5 +32  
#    print(tempCe,"°C equals to: ", tempFa,"°F")
#    input("press any key to end the program\n")
#main()