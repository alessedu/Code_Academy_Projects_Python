songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]

#Using a dict comprehension, create a dictionary called plays that goes through zip(songs, playcounts)
plays_zipped = zip(songs, playcounts)
plays = {key: value for key, value in plays_zipped}
print(plays)

# add a new entry to it.
plays["Purple Haze"] = 1
#Update the value for "Respect" to be 94
plays["Respect"] = 94

#Create a dictionary called library that has two key: value pairs:
#key "The Best Songs" with a value of plays, the dictionary you created 
#key "Sunday Feelings" with a value of an empty dictionary
library = {"The Best Songs": plays, "Sunday Feelings": {}}
print(library)