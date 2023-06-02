# -*- coding: utf-8 -*-
"""
@author: Heba
"""
"We need to compare all our risk factors and found out what makes a bigger risk than other things, then create some sort of score (well that doesn't sound like the right word but yk, something to weigh their risk')"
"Can keep track of how at risk they are using this"
RiskFactor = 0

"user input for height and weight (metric scale)"
weight = float(input("Enter your weight (Kilograms): "))
height = float(input("Enter your height (Meters): "))
sex = (input("M or F: "))

"calculate their bmi, based on given weight/height"
def calcBMI(weight, height):
    bmi = round(weight/(height**2), 2)
    return bmi

"based on the bmi, group them into a category"
def categorize(bmi):
    if bmi < 16:
        return "Severely Underweight"
    elif 16 <= bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal"
    elif 25 <= bmi < 30:
        return "Overweight"
    elif 30 <= bmi < 35:
        return "Obesity class 1"
    else:
        return "Extremely Obese"
        
bmi = calcBMI(weight, height)
weightCategory = categorize(bmi)

"output the results"
print("your BMI is: ", bmi)
print("Your BMI indicates that you are: ", weightCategory)

"bmi and diabetes predictor"
if sex == "F" and 24.4 < bmi:
    RiskFactor += 1;
    print("You are at significantly higher risk of diabetes due to your BMI")
            
elif sex == "M" and 25 < bmi:
    RiskFactor += 1;
    print("You are at significantly higher risk of diabetes due to your BMI")
        
else:
    print("Your BMI does not indicate contribution to any extreme risk of diabetes")


print("Risk Factor: ", RiskFactor)
        