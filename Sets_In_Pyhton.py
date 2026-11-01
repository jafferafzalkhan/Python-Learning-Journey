# Sets in Python

# A set in Python is a collection of unique elements.
# Sets are unordered, meaning their elements do not have a fixed position.
# Sets do not allow duplicate values.
# Sets are mutable, meaning we can add or remove elements after creation.
# Sets cannot be accessed using indexes because they are unordered.

# Creating a set
my_set = {10, 20, 30, 40, 50}

print(my_set)
# Output: {10, 20, 30, 40, 50}


# Creating a set with duplicate values
# Duplicate elements are automatically removed.
my_set = {10, 20, 20, 30, 30, 40}

print(my_set)
# Output: {10, 20, 30, 40}


# Creating an empty set
# Use set() to create an empty set.
# {} creates an empty dictionary, not a set.
empty_set = set()

print(empty_set)
# Output: set()


# Adding an element to a set
# The add() method inserts a single element into the set.
my_set = {10, 20, 30}
my_set.add(40)

print(my_set)
# Output: {10, 20, 30, 40}


# Adding multiple elements to a set
# The update() method adds multiple elements from an iterable.
my_set.update([50, 60, 70])

print(my_set)
# Output: {10, 20, 30, 40, 50, 60, 70}


# Removing an element using remove()
# The remove() method removes the specified element.
# It raises a KeyError if the element does not exist.
my_set.remove(20)

print(my_set)
# Output: {10, 30, 40, 50, 60, 70}


# Removing an element using discard()
# The discard() method removes the specified element if it exists.
# It does not raise an error if the element is missing.
my_set.discard(100)

print(my_set)
# Output: {10, 30, 40, 50, 60, 70}


# Removing an arbitrary element using pop()
# The pop() method removes and returns an arbitrary element.
# Since sets are unordered, we cannot predict which element will be removed.
removed_item = my_set.pop()

print(removed_item)
print(my_set)


# Removing all elements using clear()
# The clear() method removes every element from the set.
my_set.clear()

print(my_set)
# Output: set()


# Set Methods


# 1. add() method:
# Adds a single element to the set.
my_set = {10, 20, 30}
my_set.add(40)
print(my_set)


# 2. update() method:
# Adds multiple elements from one or more iterables.
my_set.update([40, 50], {60, 70})
print(my_set)


# 3. remove() method:
# Removes the specified element.
# Raises KeyError if the element does not exist.
my_set.remove(20)
print(my_set)


# 4. discard() method:
# Removes the specified element if it exists.
# Does not raise an error if the element is missing.
my_set.discard(100)
print(my_set)


# 5. pop() method:
# Removes and returns an arbitrary element.
removed_item = my_set.pop()
print(removed_item)
print(my_set)


# 6. clear() method:
# Removes all elements from the set.
my_set.clear()
print(my_set)
# Output: set()


# 7. copy() method:
# Creates a shallow copy of the set.
original_set = {10, 20, 30}
new_set = original_set.copy()

print(new_set)
# Output: {10, 20, 30}


# 8. union() method:
# Returns a new set containing all unique elements from both sets.
set_a = {10, 20, 30}
set_b = {30, 40, 50}

print(set_a.union(set_b))
# Output: {10, 20, 30, 40, 50}


# 9. intersection() method:
# Returns a new set containing only the elements common to both sets.
print(set_a.intersection(set_b))
# Output: {30}


# 10. difference() method:
# Returns elements present in the first set but not in the second set.
print(set_a.difference(set_b))
# Output: {10, 20}


# 11. symmetric_difference() method:
# Returns elements that are present in either set, but not in both.
print(set_a.symmetric_difference(set_b))
# Output: {10, 20, 40, 50}


# 12. intersection_update() method:
# Updates the original set to keep only common elements.
set_a = {10, 20, 30}
set_a.intersection_update({20, 30, 40})

print(set_a)
# Output: {20, 30}


# 13. difference_update() method:
# Removes elements from the original set that are present in another set.
set_a = {10, 20, 30}
set_a.difference_update({20, 30})

print(set_a)
# Output: {10}


# 14. symmetric_difference_update() method:
# Updates the original set with elements found in either set, but not both.
set_a = {10, 20, 30}
set_a.symmetric_difference_update({30, 40, 50})

print(set_a)
# Output: {10, 20, 40, 50}


# 15. isdisjoint() method:
# Returns True if the two sets have no common elements.
set_a = {10, 20}
set_b = {30, 40}

print(set_a.isdisjoint(set_b))
# Output: True


# 16. issubset() method:
# Returns True if every element of the first set is present in the second set.
set_a = {10, 20}
set_b = {10, 20, 30, 40}

print(set_a.issubset(set_b))
# Output: True


# 17. issuperset() method:
# Returns True if the set contains every element of the other set.
print(set_b.issuperset(set_a))
# Output: True


# Built-in Functions Used with Sets


# 1. len() function:
# Returns the number of elements in the set.
my_set = {10, 20, 30, 40}
print(len(my_set))
# Output: 4


# 2. type() function:
# Returns the data type of the object.
print(type(my_set))
# Output: <class 'set'>


# 3. max() function:
# Returns the largest element in the set.
print(max(my_set))
# Output: 40


# 4. min() function:
# Returns the smallest element in the set.
print(min(my_set))
# Output: 10


# 5. sum() function:
# Returns the sum of all numeric elements.
print(sum(my_set))
# Output: 100


# 6. sorted() function:
# Returns a sorted list of the set elements.
print(sorted(my_set))
# Output: [10, 20, 30, 40]


# 7. any() function:
# Returns True if at least one element is truthy.
print(any(my_set))
# Output: True


# 8. all() function:
# Returns True if every element is truthy.
print(all(my_set))
# Output: True


# 9. list() function:
# Converts the set into a list.
print(list(my_set))
# Output: [10, 20, 30, 40]
# Note: The order of elements may vary.


# 10. tuple() function:
# Converts the set into a tuple.
print(tuple(my_set))
# Note: The order of elements may vary.


# Checking membership in a set
# Use the in operator to check whether an element exists.
my_set = {10, 20, 30}

print(20 in my_set)
# Output: True

print(50 in my_set)
# Output: False


# Looping through a set
# A for loop visits each element in the set.
# The order of elements is not guaranteed.
for item in my_set:
    print(item)