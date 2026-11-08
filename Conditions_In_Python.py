# condition in python are used to perform different actions based on different conditions.
# The most common conditional statements in Python are:
# if statement

# if statement is used to test a specific condition. 
# If the condition evaluates to True, the block of code within the if statement is executed. 
# If the condition evaluates to False, the block of code is skipped.

age = 20

if age >= 18:
    print("You are eligible to vote.")
 
# if else Statement is used to test a specific condition and
#  provide an alternative block of code to execute if the condition evaluates to False.
# age = 16

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

# if elseif Statement is used to test multiple conditions.
marks = 75

if marks >= 90:
    print("Grade A")

elif marks >= 75:
    print("Grade B")

elif marks >= 50:
    print("Grade C")

else:
    print("Fail")

# nested if statement is used to test multiple conditions within another if statement.
age = 22
has_license = True

if age >= 18:
    if has_license == True:
        print("You can drive.")
    else:
        print("You need a driving license.")
else:
    print("You are too young to drive.")