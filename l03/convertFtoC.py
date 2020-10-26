#convert.py
#converts a temperature from Fahrenheit to Celsius - because other than in the textbook I cant deal with °F :)
#by Alexander Huber
#exercises 1 & 2

def main():
    print("this programm converts a Temperatur given in °F into °C")
    tempFa = eval(input("Enter a temperature in °F: "))
    tempCe = (tempFa - 32) * 5/9   
    print(tempFa,"°F equals to: ", tempCe,"°C")
    input("press any key to end the program\n")
main()