# BMI = weight in kgs / (height in m)^2

weight = float(input("Enter weight in kgs\n"))
height = float(input("Enter height in meters\n"))

bmi = weight / (height ** 2)
print(f"BMI is {bmi}")