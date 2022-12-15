# Your code below:
#create a list called toppings
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"] 

# create a list called prices 
prices = [2, 6, 1, 3, 2, 7, 2]

num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)

#Find the length of the toppings list and store it in a variable called num_pizzas.
num_pizzas = len(toppings)
print(num_pizzas)

#Print the string We sell [num_pizzas] different kinds of pizza!, where [num_pizzas] represents the value of our variable num_pizzas.
print("We sell ", num_pizzas, "different kinds of pizza!")

#Use the existing data about the pizza toppings and prices to create a new two-dimensional list called pizza_and_prices.
pizza_prices = [[2,"pepperoni"],[6,"pineapple"],[1,"cheese"],[3,"sausage"],[2,"olives"],[7,"anchovies"],[2,"mushrooms"]]
print(pizza_prices)

#Sort pizza_and_prices so that the pizzas are in the order of increasing price (ascending).
pizza_prices.sort()
print(pizza_prices)

#Store the first element of pizza_and_prices in a variable called cheapest_pizza.
cheapest_pizza = pizza_prices[0]
print(cheapest_pizza)

#Get the last item of the pizza_and_prices list and store it in a variable called priciest_pizza.
priciest_pizza = pizza_prices[-1]
print(priciest_pizza)

#It looks like the most expensive pizza from the previous step was our very last "anchovies" slice. Remove it from our pizza_and_prices list since the man bought the last slice.
pizza_prices.pop()
print(pizza_prices)

#you want to add a new topping called "peppers". Make sure to position it relative to the rest of the sorted data in pizza_and_prices
pizza_prices.insert(4,[2.5,"peppers"])
print(pizza_prices)

#Slice the pizza_and_prices list and store the 3 lowest cost pizzas in a list called three_cheapest.
three_cheapest = pizza_prices[0:3]
print(three_cheapest)





