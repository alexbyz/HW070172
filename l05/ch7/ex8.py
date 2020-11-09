#ex8

def main():
    age, cit = eval(input("enter age, duration of citizenship "))

    if cit >= 7 and age >=25:
        print("you are eligible for the House")
        if cit >= 9 and age >=35:
            print("you are eligible for the Senat")    
        elif cit <9 and age >=35:
            print("you need {0} more years of citizenship in the US to be eligible for the Senat".format(9-cit))  
        elif cit >9 and age <=35:
            print("you are {0}year(s) too young to be eligible for the Senat".format(35-age)) 
        else:
            print("you are {0}year(s) too young and you need {1} more years of citizenship to be eligible for the House\n".format((35-age),(9-cit)))
    elif cit <7 and age >=25:
        print("you need {0} more years of citizenship in the US to be eligible for the House".format(7-cit))  
    elif cit >7 and age <=25:
        print("you are {0}year(s) too young to be eligible for the House".format(25-age)) 
    else:
        print("you are {0}year(s) too young and you need {1} more years of citizenship to be eligible for the House\n".format((25-age),(7-cit)))

main()