"""
You are a student and you are trying to organize your subjects 
and grades using Python. Let’s explore what we’ve learned about lists to organize your subjects and scores.
"""

last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Your code below: 
#Create a list called subjects and fill it with the classes you are taking:
subjects = ["physics", "calculus", "poetry", "history"]
#  Create a list called grades and fill it with your scores:
grades = [98, 97, 85, 88]
# create a two-dimensional list to combine subjects and grades
gradebook = [["physics, 98"], ["calculus", 97], ["poetry", 85], ["history", 88]]
# Use append to add ["computer_science", 100] to gradebook.
gradebook.append(["computer science",100])
# Use append to add ["visual arts", 93] to gradebook.
gradebook.append(["visual arts", 93])
# Access the index of the grade for your visual arts class and modify it to be 5 points greater.
gradebook[5][1]= 98
#You decided to switch from a numerical grade value to a Pass/Fail option for your poetry class.Find the grade value in your gradebook for your poetry class and use the .remove() method to delete it.
gradebook[2].remove(85)
# Use the .append() method to then add a new "Pass" value to the sublist where your poetry class is located.
gradebook[2].append("Pass")
#Create a new variable full_gradebook that combines both last_semester_gradebook and gradebook
print(gradebook)

full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook)