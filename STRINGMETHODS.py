# using string in python has different methods

STR1 = "Hello, World!"
STR2 = 'Python is great for string manipulation.'
STR3 = '''This is a multi-line string.
It can span multiple lines.'''
print(STR1)
print(STR2)
print(STR3)

###########################################################################################################

# String slicing is a technique used to extract a portion of a string. 
# In Python, you can use slicing to get a substring from a string. The syntax for slicing is:

name = "Python Programming"
name_slice1 = name[7]  # This will extract characters from index 7
print(name_slice1)  # Output: P

name_slice2 = name[0:6]  # This will extract characters from index 0 to 5
name_slice = name[0:6]  # This will extract characters from index 0 to 5
print(name_slice)  # Output: Python 

name_slice2 = name[-3:-1]  # This will extract characters from index -3 to -1
print(name_slice2)  # Output: in  

##########################################################

# slicing with skip value
name_slice3 = name[0:6:2]  # This will extract characters from index 0 to 5 with a step of 2
print(name_slice3)  # Output: Pto

name_slice4 = name[::3]  # This will extract every third character from the string
print(name_slice4)  # Output: Ph oai

################################################################################################################

# string functions in python are used to perform various operations on strings.
# Some of the commonly used string functions are:

# .upper() - This function converts all the characters in a string to uppercase.
alpha_1 = "hello"
print(alpha_1.upper())

# .lower() - This function converts all the characters in a string to lowercase.
alpha_2 = "HELlo"
print(alpha_2.lower())

# .capitalize() - This function capitalizes the first character of a string and converts the rest to lowercase.
alpha_3 = "hello world"
print(alpha_3.capitalize())

# .title() - This function capitalizes the first character of each word in a string.
alpha_4 = "hello world"
print(alpha_4.title())

# .swapcase() - This function swaps the case of each character in a string. Uppercase characters become lowercase and vice versa.
alpha_5 = "HeLlo WoRld"
print(alpha_5.swapcase())

#.casefold() - This function is used to perform case-insensitive string comparisons. 
# It converts the string to a casefolded version, which is a more aggressive form of lowercase.
alpha_6 = "HELLO WORLD"
print(alpha_6.casefold())


# finding and searching in strings can be done using various methods. Some of the commonly used methods are:

# .find() - This function returns the index of the first occurrence of a substring in a string. If the substring is not found, it returns -1.
alpha_7 = "Hello, World World!"
print(alpha_7.find("World"))  # Output: 7
print(alpha_7.find("Python"))  # Output: -1

# .rfind() - This function returns the index of the last occurrence of a substring in a string. If the substring is not found, it returns -1.
print(alpha_7.rfind("World"))  # Output: 13
print(alpha_7.rfind("Python"))  # Output: -1

# .index() - This function returns the index of the first occurrence of a substring in a string. If the substring is not found, it raises a ValueError.
alpha_8 = "Hello, World! World"   
print(alpha_8.index("World"))  # Output: 7

#.rindex() - This function returns the index of the last occurrence of a substring in a string. If the substring is not found, it raises a ValueError.
print(alpha_8.rindex("World"))  # Output: 13    


# .count() - This function returns the number of occurrences of a substring in a string.
alpha_9 = "Hello,    World! World"
print(alpha_9.count("World"))  # Output: 2

# .startswith() - This function checks if a string starts with a specified substring. It returns True if it does, and False otherwise.
alpha_10 = "Hello, World!"
print(alpha_10.startswith("Hello"))  # Output: True

# .endswith() - This function checks if a string ends with a specified substring. It returns True if it does, and False otherwise.
alpha_11 = "Hello, World!"
print(alpha_11.endswith("World!"))  # Output: True

# .replace() - This function replaces all occurrences of a specified substring with another substring.
alpha_12 = "Hello, World! World"
print(alpha_12.replace("World", "Python"))  # Output: Hello, Python!

# .strip() - This function removes leading and trailing whitespace characters from a string.
alpha_13 = "  Hello, World!  "
print(alpha_13.strip())  # Output: Hello, World!

# .removeprefix() - This function removes all occurrences of a specified substring from the beginning of a string.
alpha_14 = "Hello, World! World"
print(alpha_14.removeprefix("Hello, "))  # Output: World! World

# .removesuffix() - This function removes all occurrences of a specified substring from the end of a string.
alpha_15 = "Hello, World! World"
print(alpha_15.removesuffix(" World"))  # Output: Hello, World! 



# .split() - This function splits a string into a list of substrings based on a specified delimiter. By default, it splits on whitespace.
alpha_16 = "Hello, World! World"
print(alpha_16.split())  # Output: ['Hello,', 'World!', 'World']
print(alpha_16.split(","))  # Output: ['Hello', ' World! World']

