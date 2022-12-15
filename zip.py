owners = ["Jenny", "Alexus", "Sam", "Grace"]
dogs_names = ["Elphonse", "Dr. Doggy DDS", "Carter", "Ralph"]

#The zip() function takes two (or more) lists as inputs and returns an object that contains a list of pairs. 
names_and_dog_names = zip(owners,dogs_names)
#If we were to then examine this new variable names_and_heights, we would find it looks a bit strange:This zip object contains the location of this variable in our computer’s memory.
print(names_and_dog_names)

#convert this object into a useable list by using the built-in function list():
list_of_names_and_dogs_names = list(names_and_dog_names)
#Our inner lists don’t use square brackets [ ] around the values. This is because 
#they have been converted into tuples (an immutable type of list).
print(list_of_names_and_dogs_names)