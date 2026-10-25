#Tuples in Python are immutable sequences, meaning their contents cannot be changed after creation.
my_tuple = (1, 2, "Jaffer", 4, 5)
print(my_tuple)

# Accessing elements in a tuple
print(my_tuple[0])  # Output: 1
print(my_tuple[-1])  # Output: 5

# Slicing a tuple
print(my_tuple[0:3])  # Output: (1, 2, 3)

# Tuples are immutable, so you cannot change their content
# my_tuple[0] = 10  # This will raise an error

# Counting occurrences of an element in a tuple
print(my_tuple.count(2))  # Output: 1

# Finding the index of an element in a tuple
print(my_tuple.index("Jaffer"))  # Output: 2

numbers = (10, 20, 30, 20, 40, 20)

result = numbers.count(20)
print(result)

# Finding index of particular element in a tuple
print(numbers.index(30))
print(numbers.index(20))


# finding length of the tuples 
print(len(numbers))

# we can find max value in tuples 
print(max(numbers))

# we can find min value in tuples
print(min(numbers))

#we can find sum of all the values in tuples
print(sum(numbers))

# Returns a new sorted list, not a tuple
print(sorted(numbers))
print(sorted(numbers, reverse=True))

numbers = tuple([10, 20, 30])

print(numbers)