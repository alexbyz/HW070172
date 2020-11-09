#ex5

def bmi(weight, hight):
    return (weight * 720 ) / (hight**2)

def main():
    weight, hight = eval(input("enter a weight in pounds and a hight in inches (w,h)"))
    
    vBmi = bmi(float(weight), float(hight))
    print(vBmi)

    if vBmi < 19:
        print("BMI too low")
    elif vBmi >= 19 and vBmi <=25:
        print("BMI is fine")
    else:
        print("BMI is to heigh")

main()