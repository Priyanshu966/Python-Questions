principal = int(input("Enter the amount borrowed\n"))
years = float(input("Enter the period in years\n"))
rate = float(input("Enter rate of interest\n"))

interest = principal * rate * years / 100
print(f"Simple interest on principal amount ${principal} for a period of {years} years at the rate of {rate}% is ${interest}")
