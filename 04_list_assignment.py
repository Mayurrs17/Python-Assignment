# TUPLE DATATYPE ASSIGNMENT
# =========================

# SOLVED EXAMPLE
# --------------
# Example: Calculate sum and product of tuple values
print("SOLVED EXAMPLE:")
print("Calculate sum and product of tuple values")
t = (2, 4, 6, 8, 10)
s = sum(t)
p = 1
for v in t:
    p *= v
print("Tuple:", t)
print("Sum =", s)
print("Product =", p)
print("-" * 50)

# ASSIGNMENT QUESTIONS
# ====================

# Question 1: Create a tuple of first 10 natural numbers
print("Question 1: Create a tuple of first 10 natural numbers")
t1 = tuple(range(1, 11))
print(t1)

# Question 2: Find the length of tuple (1,2,3,4,5,6,7,8,9,10)
print("\nQuestion 2: Find the length of tuple (1,2,3,4,5,6,7,8,9,10)")
t2 = (1,2,3,4,5,6,7,8,9,10)
print("Length =", len(t2))

# Question 3: Access the 3rd element from tuple ('a','b','c','d','e')
print("\nQuestion 3: Access the 3rd element from tuple ('a','b','c','d','e')")
t3 = ('a','b','c','d','e')
print("3rd element is:", t3[2])

# Question 4: Find the maximum value in tuple (23,45,12,67,34,89,56)
print("\nQuestion 4: Find the maximum value in tuple (23,45,12,67,34,89,56)")
t4 = (23,45,12,67,34,89,56)
print("Maximum =", max(t4))

# Question 5: Count how many times 5 appears in (1,5,2,5,3,5,4,5,6)
print("\nQuestion 5: Count how many times 5 appears in (1,5,2,5,3,5,4,5,6)")
t5 = (1,5,2,5,3,5,4,5,6)
print("5 appears", t5.count(5), "times")

# Question 6: Create a tuple of mixed data types (int, float, string, bool)
print("\nQuestion 6: Create a tuple of mixed data types (int, float, string, bool)")
t6 = (10, 3.5, "Python", True)
print(t6)

# Question 7: Find the index of element 'python' in ('java','python','c++','javascript')
print("\nQuestion 7: Find the index of element 'python' in ('java','python','c++','javascript')")
t7 = ('java','python','c++','javascript')
print("Index of 'python' =", t7.index("python"))

# Question 8: Check if 25 exists in tuple (10,20,30,40,50)
print("\nQuestion 8: Check if 25 exists in tuple (10,20,30,40,50)")
t8 = (10,20,30,40,50)
print("Does 25 exist?", 25 in t8)

# Question 9: Create a tuple of first 5 even numbers
print("\nQuestion 9: Create a tuple of first 5 even numbers")
t9 = (2,4,6,8,10)
print(t9)

# Question 10: Find the average of numbers in tuple (15,23,31,42,56,78)
print("\nQuestion 10: Find the average of numbers in tuple (15,23,31,42,56,78)")
t10 = (15,23,31,42,56,78)
avg = sum(t10)/len(t10)
print("Average =", avg)

