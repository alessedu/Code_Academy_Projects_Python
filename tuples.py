my_info = ('Aless', 'UTSA', 'Developer')
print(my_info)

# Access Information 
print(my_info[0])
print(my_info[1])
print(my_info[-1])

#unpacking a tuple
name, school, occupation = my_info
print(name)
print(school)
print(occupation)

# Creating a one element tuple
#wrong way
one_element_tuple = (7)
print(one_element_tuple)

#correct way
one_element_tuple = (7,)
print(one_element_tuple)
