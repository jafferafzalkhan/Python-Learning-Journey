# # Q1. Create variables for your full name, age, height, and student status. Print each variable with a descriptive label.

# Student_name = str(input("Enter your Full Name: "))
# Student_age = int(input("Enter your age: "))
# Student_height = float(input("Enter Your Height: "))
# Student_status = bool(input("Student Status: "))

# print("Full-Name: ", Student_name)
# print("Age: ", Student_age)
# print("Height: ", Student_height)
# print("Student_status: ", Student_status)

# # [ ] Q2. Create five variables containing an integer, float, string, Boolean, and None value. Print the data type of each using type().

# var1 = 2878
# var2 = 22.333333
# var3 = "fyghu"
# var4 = True
# var5 = None
# print(type(var1))
# print(type(var2))
# print(type(var3))
# print(type(var4))
# print(type(var5))

# # [ ] Q3. Predict the output: x = 15; y = x; x = 30. Print x and y. Explain why they differ.
# x = 15
# # y = x
# # x = 30
# # print("x:", x)
# # print("y:", y)
# # # Answer :-  Variable y contains 15, and variable x contains 30 because Python executes code line by line. 
# # # When we assign y = x, the current value of x (15) is copied into y before we update x to 30


# # # [ ] Q4. Create a variable whose name starts with an underscore. Store your favourite programming language and print it.
# # _Pyton = "javascript"
# # print(f"my favourite Programming language is: {_Pyton}")

# # [ ] Q5. Store the price of three products in variables. Calculate and print their total price.
# Products = {
#     "product_1": 2000,
#     "product_2": 300,
#     "product_3": 4400,
# }

# print(sum(Products.values()))


# # Part 2 — Operators
# # [ ] Q6. Predict the output of 15 + 4, 15 - 4, 15 * 4, 15 / 4, 15 // 4, 15 % 4, and 15 ** 2.
# num_1 = 15
# print(num_1 + 4) # 19
# print(num_1 - 4) # 11
# print(num_1 * 4) # 60
# print(num_1 / 4) # 3.75
# print(num_1 // 4) # 3
# print(num_1 % 4)  # 3
# print(num_1 ** 4) #50625

# # [ ] Q7. Take two numbers as input and print their sum, difference, product, and quotient.
# Num_1 = int(input("Enter The number: "))
# Num_2 = int(input("Enter The number: "))
# total = Num_1 + Num_2
# difference = Num_1 - Num_2
# product = Num_1 * Num_2
# quotient = Num_1 / Num_2
# print(f"Sum: {total}")
# print(f"Difference: {difference}")
# print(f"Product: {product}")
# print(f"Quotient: {quotient}")

# # # [ ] Q8. Calculate the area and perimeter of a rectangle with length 25 and width 12.
# # length = 25
# # width = 12
# # area_of_rectangle = length * width
# # primeter_of_rectangle = (2*(length + width))
# # print(f"area of rectangle is : {area_of_rectangle}")
# # print(f"perimeter of rectangle is : {primeter_of_rectangle}")

# # # [ ] Q9. Calculate the area of a circle with radius 14 using 3.14 × radius².
# radius = 14 
# calculate_circle = 3.14 * radius**2
# print(f"area of the circle is : {calculate_circle}")

# [ ] Q10. A student scores 78, 85, and 92 in three subjects. Calculate the total and average marks.
students_progress = {
    "English" : 79,
    "Maths" : 85,
    "python" : 99
}

Total = sum(students_progress.values())
average_marks = Total/3

print(Total)
print(average_marks)


# [ ] Q11. Predict the output of a = 10; a += 5; a *= 2; a -= 4; a //= 4. Print a.
a = 10
a += 5    # a = 10 + 5 = 15
a *= 2    # a = 15 * 2 = 30
a -= 4    # a = 30 - 4 = 26
a //= 4   # a = 26 // 4 = 6

# [ ] Q12. Predict the results of 10 > 5, 10 == 5, 10 != 5, True and False, True or False, and not True.
print(10 > 5)          # True
print(10 == 5)         # False
print(10 != 5)         # True
print(True and False)  # False
print(True or False)   # True
print(not True)        # False


# Part 3 — Strings
# [ ] Q13. Store your full name in a string. Print it in uppercase, lowercase, and title case.


# [ ] Q14. Given text = 'Python Programming', print its first character, last character, first six characters, and the string in reverse using slicing.


# [ ] Q15. Given text = '  Learn Python  ', remove the extra spaces and print the cleaned string.


# [ ] Q16. Count how many times the letter 'a' occurs in 'banana' using a string method.


# [ ] Q17. Replace 'Java' with 'Python' in the string 'I am learning Java'.


# [ ] Q18. Split 'apple,banana,mango,orange' into a list of fruits. Then join the fruits using ' - ' as a separator.


# [ ] Q19. Given text = 'python programming', print its length, check whether it starts with 'python', and check whether it contains 'gram'.



# Part 4 — Lists
# [ ] Q20. Create a list of five favourite foods. Print the first item, last item, and the list from the second to fourth items.


# [ ] Q21. Given numbers = [10, 20, 30, 40], change 20 to 25 and print the updated list.


# [ ] Q22. Create a list of three colours. Add one colour using append(), insert another at index 1, and extend the list with two more colours.


# [ ] Q23. Given numbers = [10, 20, 30, 20, 40], remove the first 20, then remove and print the last element.


# [ ] Q24. Given numbers = [5, 2, 8, 1, 9], sort the list in ascending order, then reverse it.


# [ ] Q25. Create a list of five numbers. Print its length, maximum, minimum, sum, and sorted version using built-in functions.


# [ ] Q26. Given numbers = [10, 20, 30, 40, 50], use slicing to create a list of the first three elements, the last two elements, and the reversed list.



# Part 5 — Tuples
# [ ] Q27. Create a tuple containing your name, age, and city. Print its type and length.


# [ ] Q28. Given values = (10, 20, 30, 40, 50), print the first item, last item, and middle three items using indexing and slicing.


# [ ] Q29. Given numbers = (10, 20, 10, 30, 10, 40), count how many times 10 appears and find the index of 30.


# [ ] Q30. Create a tuple with one element containing the number 5. Explain why (5,) is a tuple but (5) is an integer.



# Part 6 — Dictionaries
# [ ] Q31. Create a dictionary containing your name, age, city, and favourite language. Print the value of each key.


# [ ] Q32. Given student = {'name': 'Ali', 'marks': 75}, add a city key, update marks to 90, and print the dictionary.


# [ ] Q33. Given data = {'a': 10, 'b': 20, 'c': 30}, print all keys, all values, and all key-value pairs. Convert the values into a list.


# [ ] Q34. Given items = {'pen': 10, 'book': 50, 'bag': 500}, remove 'book' using pop(), print the removed value, and display the remaining dictionary.


# [ ] Q35. Create a dictionary with {'name': 'Jaffer', 'age': 23}. Use get() and setdefault() to access existing and missing keys. Print the dictionary after each operation.



# Part 7 — Sets
# [ ] Q36. Create a set containing 10, 20, 30, 20, 40, 10, 50. Print the set and explain what happened to duplicate values.


# [ ] Q37. Create an empty set. Add 10 and 20 using add(), then add 30, 40, and 50 using update(). Print the set.


# [ ] Q38. Given values = {10, 20, 30, 40, 50}, remove 20 using remove(), then try discard(100). Explain the difference between remove() and discard().


# [ ] Q39. Given A = {1, 2, 3, 4} and B = {3, 4, 5, 6}, find their union, intersection, difference A - B, and symmetric difference.


# [ ] Q40. Given A = {10, 20} and B = {10, 20, 30, 40}, use issubset(), issuperset(), and isdisjoint(). Predict the results and explain each.