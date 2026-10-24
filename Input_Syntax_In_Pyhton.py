#basic syntax of taking input from user in python

Input1 = input("Enter your name: ")
print("Hello, " + Input1 + "!")

# taking input in different way of data types
Input2 = int(input("Enter your age: ")) # takes integer input
Input3 = float(input("Enter your height: ")) # takes float input
Input4 = input("Enter your favorite color: ") # takes string input
Input5 = bool(input("Do you like Python? (True/False): ")) # takes boolean input
Input6 = complex(input("Enter a complex number: ")) # takes complex input
print("Your age is:", Input2)
print("Your height is:", Input3)
print("Your favorite color is:", Input4)
print("Your age is:", Input2)
print("Your height is:", Input3)
print("Your favorite color is:", Input4)
print("Your age is:", Input2)
print("Your height is:", Input3)
print("Your favorite color is:", Input4)

# string prefix in pyhton

# f — Formatted string literal (f-string)
print(f"Hello,{Input1}!")
print(r"C:\Users\jaffer afzal khan\OneDrive\Documents\Python learning")
bytes_1 = b"Hello, World!"
print(bytes_1)

print(f"calculating the sum of two numbers {Input2} and {Input3}")
print(f"Calculating the sum of two numbers {Input2} + {Input3} = {Input2 + Input3}")

