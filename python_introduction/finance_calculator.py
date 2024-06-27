monthly_incom = int(input('Enter your monthly income: '))
monthly_expenses = int(input('Enter your total monthly expenses: '))
monthly_savings = monthly_incom - monthly_expenses
Projected_savings = monthly_savings * 12 + monthly_savings * 12 * 0.05
print(f'Your monthly savings are {monthly_savings}')
print (f'Projected savings after one year, with interest, is:{Projected_savings}')