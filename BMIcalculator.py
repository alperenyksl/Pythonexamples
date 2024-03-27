def calculate_bmi(weight, height_cm):
    height_m = height_cm / 100
    bmi = weight / (height_m ** 2)
    return bmi

weight = float(input("Enter your weight in kg: "))
height_cm = float(input("Enter your height in cm: "))

bmi = calculate_bmi(weight, height_cm)
print("Your BMI is: {:.2f}".format(bmi))
