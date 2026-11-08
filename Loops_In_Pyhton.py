
"""
                 LOOPS IN PYTHON
================================================

1. WHAT ARE LOOPS?

A loop in Python is used to execute a block of code
repeatedly until a particular condition is satisfied
or a sequence is completed.

Example:

Without Loop:
"""

print("Hello World")
print("Hello World")
print("Hello World")
print("Hello World")
print("Hello World")

"""
Using Loop:
"""

for i in range(5):
    print("Hello World")

"""
Output:
Hello World
Hello World
Hello World
Hello World
Hello World


================================================
2. TYPES OF LOOPS IN PYTHON
================================================

Python has two main types of loops:

1. For Loop
2. While Loop


================================================
3. FOR LOOP
================================================

A for loop is used to iterate over a sequence such as
a list, string, tuple, or range.

SYNTAX:

for variable in sequence:
    # Code to execute

Example 1: Print numbers from 1 to 5
"""

for i in range(1, 6):
    print(i)

"""
Output:
1
2
3
4
5

EXPLANATION:

- for: Starts the loop.
- i: Variable that stores the current value.
- range(1, 6): Generates numbers from 1 to 5.
- print(i): Prints the current value.

IMPORTANT:
range(1, 6) excludes 6 because the ending value
is always excluded.


Example 2: Print your name 5 times
"""

for i in range(5):
    print("Jaffer")

"""
Output:
Jaffer
Jaffer
Jaffer
Jaffer
Jaffer


Example 3: Print even numbers from 1 to 20
"""

for i in range(2, 21, 2):
    print(i)

"""
Output:
2
4
6
8
10
12
14
16
18
20

EXPLANATION:

range(2, 21, 2)

2  = Starting value
21 = Ending value (excluded)
2  = Increment by 2


================================================
4. WHILE LOOP
================================================

A while loop executes a block of code repeatedly
as long as the given condition is True.

SYNTAX:

while condition:
    # Code to execute
    # Update the variable

Example 1: Print numbers from 1 to 5
"""

i = 1

while i <= 5:
    print(i)
    i += 1

"""
Output:
1
2
3
4
5

EXPLANATION:

Step 1: Initialize the variable

i = 1

We assign 1 to the variable i.

Step 2: Check the condition

while i <= 5:

Python checks whether i is less than or equal to 5.

Step 3: Print the value

print(i)

Prints the current value of i.

Step 4: Increment the value

i += 1

Increases the value of i by 1.

IMPORTANT:

A while loop does not automatically increment the
variable. We need to update it manually.

If we forget to increment or update the variable,
the loop may run forever. This is called an
INFINITE LOOP.


================================================
5. DIFFERENCE BETWEEN FOR AND WHILE LOOP
================================================

FOR LOOP:

Used when iterating over a sequence or when the
number of iterations is known.

Example:
"""

for i in range(1, 6):
    print(i)

"""
WHILE LOOP:

Used when repetition depends on a condition.

Example:
"""

i = 1

while i <= 5:
    print(i)
    i += 1

"""
Both produce the same output:

1
2
3
4
5


================================================
6. REAL-WORLD EXAMPLES OF LOOPS
================================================

Example 1: Calculate the sum of numbers from 1 to 10
"""

total = 0

for i in range(1, 11):
    total += i

print("Total:", total)

"""
Output:
Total: 55

Explanation:

- total = 0 initializes the sum.
- The loop generates numbers from 1 to 10.
- total += i adds each number to the total.
- Finally, we print the result.


Example 2: Multiplication table
"""

num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)

"""
Example Output:

Enter a number: 5

5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50


Example 3: Find prime numbers from 1 to 100
"""

for num in range(2, 101):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num, end=" ")

"""
Output:

2 3 5 7 11 13 17 19 23 29 31 37 41 43 47
53 59 61 67 71 73 79 83 89 97

Explanation:

- The outer loop selects numbers from 2 to 100.
- The inner loop checks whether a number is divisible
  by any number between 2 and num - 1.
- If divisible, break stops the inner loop.
- If the inner loop finishes without break,
  its else block executes and prints the prime number.


================================================
7. LOOP CONTROL STATEMENTS
================================================

Python provides three important loop control statements:

1. break
2. continue
3. pass


-------------------------
1. BREAK STATEMENT
-------------------------

The break statement immediately terminates the loop.
"""

for i in range(1, 6):
    if i == 3:
        break
    print(i)

"""
Output:
1
2


-------------------------
2. CONTINUE STATEMENT
-------------------------

The continue statement skips the current iteration
and moves to the next iteration.
"""

for i in range(1, 6):
    if i == 3:
        continue
    print(i)

"""
Output:
1
2
4
5


-------------------------
3. PASS STATEMENT
-------------------------

The pass statement does nothing. It is used as a
placeholder when you want to write code later.
"""

for i in range(1, 6):
    if i == 3:
        pass
    print(i)

"""
Output:
1
2
3
4
5


================================================
8. NESTED LOOPS
================================================

A loop inside another loop is called a nested loop.

Example:
"""

for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)

# """
# Output:

# 1 1
# 1 2
# 1 3
# 2 1
# 2 2
# 2 3
# 3 1
# 3 2
# 3 3

# Explanation:

# - The outer loop runs 3 times.
# - For every iteration of the outer loop,
#   the inner loop runs 3 times.
# - Total executions = 3 x 3 = 9.