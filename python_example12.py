## Example12 : examples based on List, Dictionaries, Tuples


# List
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[2:6])

numbers.append(10)
print(numbers)


vegetables = ['carrot', 'potato']
fruits = ['apple', 'orange']
combined = vegetables + fruits
print(combined)   

fruits.append('banana')  #  Adding new list
print(fruits)  


# Dictionaries
person = {'name': 'Suraj', 'age': 24, 'city': 'Mumbai'}
print(person['age'])
print(person["name"])

person["email"] = "john@gmail.com"
print(person["email"])
person["age"] = 33 
print(person['age'])


# Tuples
person = ("John", 25, "NY")
print(person[0])
print(person[-1])

cordinates = (10, 20, 30)
x, y, z = cordinates
print(x)
print(y)
print(z)


# sets
my_set = {1, 2, 2, 3}
print(my_set)

