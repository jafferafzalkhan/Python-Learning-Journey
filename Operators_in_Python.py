# Operators in Python are special symbols or keywords that perform operations on one or more operands.
#  They can be categorized into several types, including arithmetic operators, 
# comparison operators, logical operators, assignment operators, bitwise operators, and more.



# Arithimetic Operators:
# 1. Addition (+): Adds two operands.
Num1 = 10
num2  = 20
print("Addition of two number is:", Num1 + num2)

#2. Subtraction (-): Subtracts the second operand from the first.
Num1 = 10
num2  = 20
print("Subtraction of two number is:", Num1 - num2)

#3. Multiplication (*): Multiplies two operands.
Num1 = 10
num2  = 20
print("Multiplication of two number is:", Num1 * num2)

#4. Division (/): Divides the first operand by the second.
Num1 = 20
num2  = 10
print("Division of two number is:", Num1 / num2)

#5. Modulus (%): Returns the remainder of the division.
Num1 = 10
num2  = 20
print("Modulus of two number is:", Num1 % num2)

#6. Exponent (**): Raises the first operand to the power of the second.
Num1 = 10
num2  = 2
print("Exponent of two number is:", Num1 ** num2)

#7. Floor Division (//): Returns the largest possible integer from the division.
Num1 = 10
num2  = 20
print("Floor Division of two number is:", Num1 // num2)

# Comparison Operators:
# 1. Equal to (==): Returns True if both operands are equal.    
a = 10
b = 20     
print("Equal to operator result is:", a == b)   

# 2. Not equal to (!=): Returns True if both operands are not equal.
a = 10
b = 20
print("Not equal to operator result is:", a != b)

# 3. Greater than (>): Returns True if the left operand is greater than the right operand.
a = 10  
b = 20
print("Greater than operator result is:", a > b)

# 4. Less than (<): Returns True if the left operand is less than the right operand.
a = 10
b = 20
print("Less than operator result is:", a < b)

# 5. Greater than or equal to (>=): Returns True if the left operand is greater than or equal to the right operand.
a = 10
b = 20
print("Greater than or equal to operator result is:", a >= b)

# 6. Less than or equal to (<=): Returns True if the left operand is less than or equal to the right operand.
a = 10
b = 20
print("Less than or equal to operator result is:", a <= b)

# Logical Operators:
# 1. and: Returns True if both operands are True.
a = True
b = False
print("Logical AND operator result is:", a and b)

# 2. or: Returns True if at least one of the operands is True.
a = True
b = False
print("Logical OR operator result is:", a or b)

# 3. not: Returns True if the operand is False, and vice versa.
a = False
# b = True
print("Logical NOT operator result is:", not a)

# #assignment Operators:
# # 1. Assignment (=): Assigns the value of the right operand to the left operand
a = 10
print("Assignment operator result is:", a)

# # 2. Add and Assign (+=): Adds the right operand to the left operand and assigns the result to the left operand.
a = 10
a += 5
print("Add and Assign operator result is:", a)

# # 3. Subtract and Assign (-=): Subtracts the right operand from the left operand and assigns the result to the left operand.
a = 10
a -= 5
print("Subtract and Assign operator result is:", a)

# # 4. Multiply and Assign (*=): Multiplies the left operand by the right operand and assigns the result to the left operand.
a = 10
a *= 5

print("Multiply and Assign operator result is:", a)

# # 5. Divide and Assign (/=): Divides the left operand by the right operand and assigns the result to the left operand.
a = 10
a /= 5
print("Divide and Assign operator result is:", a)

# 6. Modulus and Assign (%=): Takes the modulus of the left operand by the right operand and assigns the result to the left operand.
a = 10
a %= 5
print("Modulus and Assign operator result is:", a)

# # 7. Exponent and Assign (**=): Raises the left operand to the power of the right operand and assigns the result to the left operand.
a = 10
a **= 5
print("Exponent and Assign operator result is:", a)

# 8. Floor Division and Assign (//=): Takes the floor division of the left operand by the right operand and assigns the result to the left operand.
a = 10
a //= 5
print("Floor Division and Assign operator result is:", a)

# # Bitwise Operators:
# 1. AND (&): Performs a bitwise AND operation on two operands.
a = 10
b = 20
print("Bitwise AND operator result is:", a & b)

# # 2. OR (|): Performs a bitwise OR operation on two operands.
# a = 10
# b = 20
# print("Bitwise OR operator result is:", a | b)

# # 3. XOR (^): Performs a bitwise XOR operation on two operands.
# a = 10
# b = 20
# print("Bitwise XOR operator result is:", a ^ b)

# 4. NOT (~): Performs a bitwise NOT operation on a single operand.
a = 10
print("Bitwise NOT operator result is:", ~a)

# 5. Left Shift (<<): Shifts the bits of the left operand to the left by the number of positions specified by the right operand.
a = 10
b = 2

print("Left Shift operator result is:", a << b)

# 6. Right Shift (>>): Shifts the bits of the left operand to the right by the number of positions specified by the right operand.
a = 10
b = 2
print("Right Shift operator result is:", a >> b)



