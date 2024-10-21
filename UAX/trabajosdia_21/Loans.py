p = 250000  # Loan given
n = 30*12 # Time of debt(given in years and transformed into months)
r = 0.05/12 # Interest rate (per year transformed into months)


# Calculating the monthly payment (M) using the formula: M = P * [r * (1 + r)^n] / [(1 + r)^n - 1]
M = p * (r * (1 + r) ** n) / ((1 + r) ** n - 1)

# Printing the calculated monthly payment and total payment for the loan.
print (f"The monthly payment for this loan is: {M}")
print (f"The total payment will be: {M*n}")