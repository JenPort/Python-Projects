# A BMI Calculator that doesn't make you feel too bad
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

# Input for Weight and Height
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

# Calculate BMI
result = calculate_bmi(weight, height)
print("Your BMI is:", result)

# Modified BMI
if result < 16.5:
    print("Underweight.")
elif 18.5 <= result <= 25.5:
    print("Normal Weight.")
elif 30 <= result <= 35.5:
    print("Overweight.")
else:
    print("Obese.")
