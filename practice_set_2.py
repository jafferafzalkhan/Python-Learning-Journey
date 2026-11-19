# 1. Write a Python program to store the names of 5 students in a list entered by the user. Display all the names.
# students = []
# for i in range(5):
#     name = input(f"Enter the name of student : ")
#     students.append(name)

# print(students)

# 2. Write a program to accept 10 numbers from the user and display them in descending order.
# Numbers = []
# for i in range(10):
#     num = int(input(f"Enter The Number {i+1} :"))
#     Numbers.append(num)
#     Numbers.sort(reverse=True)

# print(Numbers)

# 3. Write a program to find the largest and smallest numbers in a list given by the user
#  without using max() and min().
# numbers = []

# for i in range(10):
#     num_ = int(input(f"Enter The Number {i+1} :"))
#     numbers.append(num_)

# largest = numbers[0]
# smallest = numbers[0]

# for j in numbers:
#     if j > largest:
#         largest = j

#     if j < smallest:
#         smallest = j

# print("Largest Number:", largest)
# print("Smallest Number:", smallest)

# 4. Write a program to count how many even and odd numbers are present in a list.
# numbers = []

# for i in range(10):
#     num_ = int(input(f"Enter The Number {i+1} :"))
#     numbers.append(num_)

# even = 0
# odd = 0
# for num in numbers:
#     if num%2 == 0:
#        even += 1
#     else:
#        odd += 1

# print(even)
# print(odd)

# # 5. Write a program to remove duplicate elements from a list.
# list_1 = []
# for i in range(5):
#     num = int(input(f"Enter The Number {i+1} :"))
#     list_1.append(num)

# new_list = []
# for i in list_1:
#    if i not in new_list:
#       new_list.append(i)

# print(new_list)

# # find the prime number from 1 to 100
# count = 0

# for num in range(2, 101):
#     is_prime = True

#     for i in range(2, num):
#         if num % i == 0:
#             is_prime = False
#             break

#     if is_prime:
#         print(num, end=" ")
#         count += 1

# print("\nTotal prime numbers:", count)


# 6. Write a program to calculate the sum of all elements in a list without using the sum() function.
# numbers =[]

# for i in range(5):
#     input_num = int(input(f"Enter The number {i + 1} :"))
#     numbers.append(input_num)

# total = 0
# for j in numbers:
#     total += j

# print(total)    

# 7. Write a program to check whether a given element exists in a tuple or not.
# User_input = (2, 3, 4, 5, 66)

# input_1 = int(input("Enter The Number: "))
# found = False
# for i in User_input:
#     if i == User_input:
#         found = True
#         break

# if found:
#     print("the number is present")
# else:
#     print("the number is not present ")

# 8. Write a program to find the number of times a particular element appears in a tuple.
# num_1 = (2 ,4,5,6,7,8,9,7,4)

# num_user = int(input("Enter the Number:-"))

# count = 0

# for i in num_1:
#     if i == num_user:
#         count += 1

# print(f"the number you enter is appear {count} times")

# What will be the output of the following code? Explain why.
# a = (10, 20, 30, 40)
# a[1] = 50
# print(a)


# # 10. Write a program to reverse a list without using the reverse() method.
# user1 = []

# for i in range(6):
#     user_Input = int(input(f"Enter the Number {i + 1} :-"))
#     user1.append(user_Input)

# reverse_list = []

# for j in user1:
#     reverse_list.insert(0,j)

# print(user1)
# print(reverse_list)

# # Find the second-largest element in a list without using sort() or max().

# num = []

# for i in range(5):
#     inpuse = int(input(f"Enter the Number to add in a list :- "))
#     num.append(inpuse)

# largest = 0
# second_largest = 0
# third_largest = 0

# for j in num:
#     if j > largest:
#         third_largest = second_largest
#         second_largest = largest
#         largest = j

#     if j < largest and j > second_largest:
#         third_largest = second_largest
#         second_largest = j
#     if j > third_largest and j < second_largest:
#         third_largest = j

# print(largest)
# print(second_largest)
# print(third_largest)




# CHAPTER 5 – SETS & DICTIONARIES

# 1. Create a dictionary containing 5 countries as keys and their capitals as values. Allow the user to enter a
# country and display its capital.

# World_countries = {
#     "India": "New_Delhi",
#     "USA": "Washington, D.C.",
#     "France": "Paris",
#     "Japan": "Tokyo",
#     "Germany": "Berlin"
# }

# Country_Input = input("Enter The Country Name :-")

# if Country_Input in World_countries:
#     print(f"{Country_Input} Capital is {World_countries.get(Country_Input)} ")
# else:
#     print("Country Not Found")


# 2. Write a program to create a dictionary of 5 students and their marks. Display the student who scored the
# highest marks.

# Student_Dict = dict()

# for i in range(5):
#     student = input("Enter student name :- ")
#     student_Marks = int(input("Enter student marks :- "))
#     Student_Dict[student] = student_Marks

# Higest_marks = 0
# Topper_Dict = dict()
# for j in Student_Dict:
#     if Student_Dict[j] > Higest_marks:
#         Higest_marks = Student_Dict[j]
#         Topper_Dict.update({j: Higest_marks})

# print(Higest_marks)
# print(Topper_Dict)

# 3. Write a program to count the frequency of each character in a string using a dictionary.


# Frequency_Dict = {}

# word = input("Enter a string: ")

# for j in word:
#     if j in Frequency_Dict:
#         Frequency_Dict[j] += 1
#     else:
#         Frequency_Dict[j] = 1

# print(Frequency_Dict)


# # . Create an empty dictionary and allow 4 friends to enter their names and favourite programming languages.

# Friends_Dict = {}

# for i in range(4):
#     name = input("Enter your name: ")
#     language = input("Enter your favourite programming language: ")

#     Friends_Dict[name] = language

# print(Friends_Dict)

# #  What will be the output of the following code?
# s = set()
# s.add(10)
# s.add(20)
# s.add(10)
# s.add(30)
# s.add(20)
# print(s)
# print(len(s))

# 6. Write a program to find the common elements between two sets.
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
common_elements = set1 & set2
print(set1.intersection(set2))
print(common_elements)

# Write a program to find the union and intersection of two sets
union_elements = set1 | set2
print(union_elements)

# What will be the output? Explain how updating an existing dictionary key works.
a = {}
a["name"] = "Jaffer"
a["age"] = 22
a["name"] = "Rahul"
print(a)
print(len(a))

# Write a program to find the difference between two sets.
difference_elements = set1 - set2
print(difference_elements)


# Conditional Statements Questions

# 1. Write a program to find the greatest of three numbers entered by the user.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Greatest number:", a)

elif b >= a and b >= c:
    print("Greatest number:", b)

else:
    print("Greatest number:", c)


# 2. Write a program to check whether a given number is positive, negative or zero.

num = int(input("Enter a number: "))

if num > 0:
    print("Positive number")

elif num < 0:
    print("Negative number")

else:
    print("Zero")


# 3. Write a program to check whether a given year is a leap year or not.

year = int(input("Enter a year: "))

if year % 400 == 0:
    print("Leap year")

elif year % 100 == 0:
    print("Not a leap year")

elif year % 4 == 0:
    print("Leap year")

else:
    print("Not a leap year")


# 4. A student has three subjects. Write a program to calculate the percentage and check whether the student has passed or failed.
# Conditions: Minimum 40% overall and minimum 33 marks in each subject. Each subject carries 100 marks.

sub1 = int(input("Enter marks of subject 1: "))
sub2 = int(input("Enter marks of subject 2: "))
sub3 = int(input("Enter marks of subject 3: "))

total = sub1 + sub2 + sub3
percentage = (total / 300) * 100

print("Total marks:", total)
print("Percentage:", percentage)

if percentage >= 40 and sub1 >= 33 and sub2 >= 33 and sub3 >= 33:
    print("Pass")

else:
    print("Fail")


# 5. Write a program to check whether a given character is a vowel or consonant.

character = input("Enter a character: ").lower()

vowels = ("a", "e", "i", "o", "u")

if character in vowels:
    print("Vowel")

else:
    print("Consonant")


# 6. Write a program to calculate an electricity bill:
# First 100 units at Rs. 5 per unit,
# next 100 units at Rs. 7 per unit,
# and units above 200 at Rs. 10 per unit.

units = int(input("Enter electricity units: "))

if units <= 100:
    bill = units * 5

elif units <= 200:
    bill = (100 * 5) + ((units - 100) * 7)

else:
    bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)

print("Electricity bill:", bill)


# 7. Write a program to calculate grades:
# 90–100: A+
# 80–89: A
# 70–79: B
# 60–69: C
# 40–59: D
# Below 40: F

marks = int(input("Enter your marks: "))

if marks >= 90 and marks <= 100:
    print("Grade A+")

elif marks >= 80:
    print("Grade A")

elif marks >= 70:
    print("Grade B")

elif marks >= 60:
    print("Grade C")

elif marks >= 40:
    print("Grade D")

elif marks >= 0:
    print("Grade F")

else:
    print("Invalid marks")


# 8. Write a program to check whether a given username contains exactly 10 characters.

username = input("Enter your username: ")

if len(username) == 10:
    print("Valid username")

else:
    print("Username must contain exactly 10 characters")


# 9. Write a program to check whether a given number is divisible by both 5 and 11.

num = int(input("Enter a number: "))

if num % 5 == 0 and num % 11 == 0:
    print("Divisible by both 5 and 11")

else:
    print("Not divisible by both 5 and 11")


# 10. Write a program to check whether a given string contains the word "Python" or not (case-insensitive).

text = input("Enter a string: ")

if "python" in text.lower():
    print("Python is present in the string")

else:
    print("Python is not present in the string")
