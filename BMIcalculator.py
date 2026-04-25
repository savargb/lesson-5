h = float(input("Enter your height in integer"))
w = float(input("Enter your weight in integer"))

BMI  = w / (h/100)**2

print("Your BMI is:",BMI)

if BMI <=18.5:
    print("You are underweight")
if BMI <= 24.9:
    print("You are healthy")
if BMI <= 29.9:
    print("You are overweight")
if BMI <= 34.9:
    print("You are severely overwight")
if BMI <= 39.9:
    print("You are obese")
else:
    print("You are severely overweight")