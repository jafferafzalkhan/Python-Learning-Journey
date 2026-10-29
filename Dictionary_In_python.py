# Dictionary in Python

# A dictionary in Python is a collection of key-value pairs.
# Each key must be unique and is used to access its corresponding value.
# Dictionaries are mutable, which means we can add, update, and remove items
# after creating a dictionary.

# Creating a dictionary
my_dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Accessing values in a dictionary
# We can access a value by specifying its corresponding key.
print(my_dict["name"])  # Output: John


# Adding a new key-value pair
# A new key-value pair is added by assigning a value to a new key.
my_dict["email"] = "jaffar@123"

# Updating an existing key-value pair
# If the key already exists, its value will be replaced with the new value.
my_dict["age"] = 31

# Removing a key-value pair
# The del statement removes the specified key and its associated value.
del my_dict["city"]


# Dictionary Methods


# 1. get() method:
# Returns the value associated with the specified key.
# If the key does not exist, it returns None by default.
# We can also provide a custom default value.

print(my_dict.get("name"))             # Output: John
print(my_dict.get("email"))            # Output: jaffar@123
print(my_dict.get("city"))             # Output: None
print(my_dict.get("city", "Not Found")) # Output: Not Found


# 2. keys() method:
# Returns a view object containing all the keys in the dictionary.
# The view reflects changes made to the dictionary.

print(my_dict.keys())
# Output: dict_keys(['name', 'age', 'email'])


# 3. values() method:
# Returns a view object containing all the values in the dictionary.
# We can use it to access or iterate through the dictionary's values.

print(my_dict.values())
# Output: dict_values(['John', 31, 'jaffar@123'])


# 4. items() method:
# Returns a view object containing all key-value pairs as tuples.
# Each tuple contains one key and its corresponding value.

print(my_dict.items())
# Output: dict_items([('name', 'John'), ('age', 31), ('email', 'jaffar@123')])


# 5. pop() method:
# Removes the specified key from the dictionary and returns its value.
# If the key does not exist, it raises a KeyError unless a default value is provided.

removed_value = my_dict.pop("age")
print(removed_value)  # Output: 31
print(my_dict)        # Output: {'name': 'John', 'email': 'jaffar@123'}

# Removing another key using pop()
my_dict.pop("name")
print(my_dict)        # Output: {'email': 'jaffar@123'}


# 6. popitem() method:
# Removes and returns the last inserted key-value pair as a tuple.
# This method raises a KeyError if the dictionary is empty.

last_item = my_dict.popitem()

print(last_item)  # Output: ('email', 'jaffar@123')
print(my_dict)    # Output: {}


# 7. setdefault() method:
# Returns the value of the specified key if it already exists.
# If the key does not exist, it inserts the key with the given default value.
# The existing value is not changed if the key is already present.

my_dict = {"name": "Jaffer", "age": 23}

result = my_dict.setdefault("age", "23")

print(result)   # Output: 23
print(my_dict)  # Output: {'name': 'Jaffer', 'age': 23}


# Converting dictionary values into a list
# The values() method returns a view object.
# The list() function converts that view into a list.

print(list(my_dict.values()))
# Output: ['Jaffer', 23]