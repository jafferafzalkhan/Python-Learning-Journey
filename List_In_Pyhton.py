#list in pyhton are data types that can store multiple values in a single variable
my_list = [1, 2, 3, 4, 5]
print(my_list)  

# list are mutable, meaning you can change their content without changing their identity
my_list[0] = 10
print(my_list)

# slicing a list
print(my_list[0:5:2]) #slicing the list from index 0 to 4 with step 2

print(my_list[::-2]) #slicing the list from start to end with step 2

# 1. append()
numbers = [1, 2, 3]
numbers.append(4)
print(numbers)  # [1, 2, 3, 4]

# 2. extend()
numbers = [1, 2, 3]
numbers.extend([4, 5])
print(numbers)  # [1, 2, 3, 4, 5]

# 3. insert() only those numbers which are not present in the list will be inserted at the specified index
numbers = [1, 2, 4]
numbers.insert(2, 3)
print(numbers)  # [1, 2, 3, 4]

# 4. remove()
numbers = [10, 20, 30, 20]
numbers.remove(20)
print(numbers)  # [10, 30, 20]

# 5. pop()
numbers = [10, 20, 30]
removed = numbers.pop(1)
print(numbers)  # [10, 30]
print(removed)  # 20

# 6. clear()
numbers = [10, 20, 30]
numbers.clear()
print(numbers)  # []

# 7. index()
numbers = [10, 20, 30, 20]
print(numbers.index(20))  # 1

# 8. count()
numbers = [10, 20, 30, 20]
print(numbers.count(20))  # 2

# 9. sort()
numbers = [4, 1, 3, 2]
numbers.sort()
print(numbers)  # [1, 2, 3, 4]

# Sort in descending order
numbers.sort(reverse=True)
print(numbers)  # [4, 3, 2, 1]

# 10. reverse()
numbers = [1, 2, 3, 4]
numbers.reverse()
print(numbers)  # [4, 3, 2, 1]

# 11. copy()
original = [1, 2, 3,8,9,0,28,10]
new_list = original.copy()

new_list.append(4)

print(original)  # [1, 2, 3]
print(new_list)  # [1, 2, 3, 4]


new_List = original[:]  # Using slicing to copy the list=
print(new_List)  # [1, 2, 3]

sorted(new_List)
print(new_List)  # [1, 2, 3, 4, 8, 9, 10, 28] (sorted does not modify the original list)

