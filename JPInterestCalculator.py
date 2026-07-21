# Input Display the three values
principal = float(input("Enter the principal amount: "))

rate = float(input("Enter the interest rate in percentage: "))

time = float(input("Enter the time period in years: "))

# Calculate the simple interest
simpleinterest = (principal * rate * time) / 100

# Display the output
print("The calculated simple interest is:", simpleinterest)
