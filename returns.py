#Our travel application is getting really popular. 
# Some of our users have posted on social media that it would be useful if our application could help them track their budget during trips.
# We want to help them track their starting budget and let them know how much they have left after an expense.

current_budget = 3500.75
shirt_expense = 9

def print_remaining_budget(budget):
  print("Your remaining budget is: $" + str(budget))

print_remaining_budget(current_budget)

def deduct_expense(budget, expense):
  return budget-expense

new_budget_after_shirt = deduct_expense(current_budget, shirt_expense)

print_remaining_budget(new_budget_after_shirt)


