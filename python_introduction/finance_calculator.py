monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))

projected_saving = monthly_income * 12 + (monthly_income * 12 * 0.05)
print(f"Your monthly savings are ${monthly_income}.")
print(f"Projected savings after one year, with interest, is: ${projected_saving}.")