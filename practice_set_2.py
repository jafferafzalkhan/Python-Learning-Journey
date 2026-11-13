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

#  What will be the output of the following code?
s = set()
s.add(10)
s.add(20)
s.add(10)
s.add(30)
s.add(20)
print(s)
print(len(s))

