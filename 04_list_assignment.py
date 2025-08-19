# TUPLE DATATYPE ASSIGNMENT
# =========================

# SOLVED EXAMPLE
# --------------
# Example: Find total sum and product of tuple elements
print("SOLVED EXAMPLE:")
print("Find total sum and product of elements in a tuple")
nums = (2, 4, 6, 8, 10)
total = sum(nums)
mul = 1
for val in nums:
    mul *= val
print(f"Tuple: {nums}")
print(f"Sum = {total}")
print(f"Product = {mul}")
print("-" * 50)

# ASSIGNMENT QUESTIONS
# ====================

# Question 1: Create a tuple of first 10 natural numbers
print("Question 1: Create a tuple of first 10 natural numbers")
natural_nums = tuple(range(1, 11))
print(natural_nums)

# Question 2: Find the length of tuple (1,2,3,4,5,6,7,8,9,10)
print("\nQuestion 2: Find the length of tuple (1,2,3,4,5,6,7,8,9,10)")
t1 = (1,2,3,4,5,6,7,8,9,10)
length = len(t1)
print(f"Length = {length}")

# Question 3: Access the 3rd element from tuple ('a','b','c','d','e')
print("\nQuestion 3: Access the 3rd element from tuple ('a','b','c','d','e')")
letters = ('a','b','c','d','e')
third = letters[2]
print(f"3rd element is: {third}")

# Question 4: Find the maximum value in tuple (23,45,12,67,34,89,56)
print("\nQuestion 4: Find the maximum value in tuple (23,45,12,67,34,89,56)")
nums2 = (23,45,12,67,34,89,56)
max_val = max(nums2)
print(f"Maximum = {max_val}")

# Question 5: Count how many times 5 appears in (1,5,2,5,3,5,4,5,6)
print("\nQuestion 5: Count how many times 5 appears in (1,5,2,5,3,5,4,5,6)")
tuple_data = (1,5,2,5,3,5,4,5,6)
count5 = tuple_data.count(5)
print(f"5 appears {count5} times")

# Question 6: Create a tuple of mixed data types (int, float, string, bool)
print("\nQuestion 6: Create a tuple of mixed data types (int, float, string, bool)")
mixed = (10, 3.14, "Python", False)
print(mixed)

# Question 7: Find the index of element 'python' in ('java','python','c++','javascript')
print("\nQuestion 7: Find the index of element 'python' in ('java','python','c++','javascript')")
langs = ('java','python','c++','javascript')
pos = langs.index("python")
print(f"Index of 'python' = {pos}")

# Question 8: Check if 25 exists in tuple (10,20,30,40,50)
print("\nQuestion 8: Check if 25 exists in tuple (10,20,30,40,50)")
t2 = (10,20,30,40,50)
check = 25 in t2
print(f"Does 25 exist? {check}")

# Question 9: Create a tuple of first 5 even numbers
print("\nQuestion 9: Create a tuple of first 5 even numbers")
evens = (2,4,6,8,10)
print(evens)

# Question 10: Find the average of numbers in tuple (15,23,31,42,56,78)
print("\nQuestion 10: Find the average of numbers in tuple (15,23,31,42,56,78)")
marks = (15,23,31,42,56,78)
avg = sum(marks) / len(marks)
print(f"Average = {avg}")
