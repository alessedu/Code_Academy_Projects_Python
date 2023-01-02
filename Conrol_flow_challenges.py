# 1. LARGE POWER
#For the first code challenge, we are going to create a method that tests whether the result of 
# taking the power of one number to another number provides an answer which is greater than 5000.
#  We will use a conditional statement to return True if the result is greater than 5000 
# or return False if it is not. In order to accomplish this, we will need the following steps:

# Write your large_power function here:
def large_power(base, exponent):
  if base ** exponent > 5000:
    return "True"
  else:
    return "False"
print("1. Large Power Challenge")
# Uncomment these function calls to test your large_power function:
print(large_power(2, 13))
# should print True
print(large_power(2, 12))
# should print False


# 2. OVER BUDGET
#Let’s say we are trying to save some money and we are watching our budget. 
# We need to make sure that the result of our spending is less than the total amount we have allocated 
# for each of the categories. Our function will accept a parameter called budget which describes our 
# spending limit. The next four parameters describe what we are spending our money on. 
# We need to sum all of our spendings and compare it to the budget. If we have gone over budget, we will return True. 
# Otherwise we return False. Here are the steps we need:

# Write your over_budget function here:
def over_budget(budget, food_bill, electricity_bill, internet_bill, rent):
  sum = food_bill + internet_bill + electricity_bill + rent
  print("Sum: " + str(sum) + " Budget: " + str(budget))
  if sum > budget:
    return "True"
  else:
    return "False"

print("1. Over Budget Challenge")
# Uncomment these function calls to test your over_budget function:
print(over_budget(100, 20, 30, 10, 40))
# should print False
print(over_budget(80, 20, 30, 10, 30))
# should print True

# 3. Twice as large
#In this challenge, we will determine if one number is twice as large as another number. 
# To do this, we will compare the first number with two times the second number. 
def twice_as_large(num1, num2):
  if num1 > 2*num2:
    return True
  else:
    return False

print("Twice as Large Challenge")
# Uncomment these function calls to test your twice_as_large function:
print(twice_as_large(10, 5))
# should print False
print(twice_as_large(11, 5))
# should print True

#4 Divisible by 10
# If the number is divisible by 10 it will return a 0.
# if it does not return a 0 it is not divisible by 10.
def divisible_by_ten(num):
  if (num % 10 == 0):
    return True
  else:
    return False
print("4. Divisible by 10 Challenge")
print(divisible_by_ten(20))

print(divisible_by_ten(25))

#5 Not sum to 10
def not_sum_to_ten(num1, num2):
  if num1 + num2 == 10:
#  if (num1 + num2 != 10): this is also an option
    return False
  else:
    return True

print("5. Not sum to 10")
print(not_sum_to_ten(9, -1))
print(not_sum_to_ten(9, 1))
print(not_sum_to_ten(5,5))