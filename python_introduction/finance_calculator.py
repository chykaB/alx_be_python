monthly_savings = int(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

projected_saving = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
print(f"Your monthly savings are ${monthly_savings}.")
print(f"Projected savings after one year, with interest, is: ${projected_saving:.2f}")