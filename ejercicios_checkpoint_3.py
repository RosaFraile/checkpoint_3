# Exercise 1: Create a string, number, list, and boolean, each stored in their own variable.

full_name = 'Rosa Fraile Garcia'
age = 56
children = ['Soraya', 'Erik', 'Joel']
married = True

# Exercise 2: Use an index to grab the first 3 letters in your string, store that in a variable. 

nick_name = full_name[0:3]

# Exercise 3: Use an index to grab the first element from your list.

first_child = children[0]

# Exercise 4: Create a new number variable that adds 10 to your original number.

more_age = age + 10

# Exercise 5: Use an index to get the last element in your list.

last_child = children[2]

# Exercise 6: Use split to transform the following string into a list.
#	names = 'harry,alex,susie,jared,gail,conner'

names = 'harry,alex,susie,jared,gail,conner'

list_names = names.split(',')

# Exercise 7: Get the first word from your string using indexes. Use the upper function to transform the letters into uppercase. Create a new string that takes the uppercase word and the rest of the original string.

new_name = full_name[:4].upper() + full_name[4:]

# Exercise 8: Use string interpolation to print out a sentence that contains your number variable.

sentence = f'My age is {age}'
print(sentence)

# Exercise 9: Print “hello world”.

print('Hello world')