# SET DATATYPE ASSIGNMENT
# ======================

# SOLVED EXAMPLE
# --------------
# Question: Find the union of two sets
print("SOLVED EXAMPLE:")
print("Find the union of two sets")
s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}
union_s = s1.union(s2)
print(f"Set 1: {s1}")
print(f"Set 2: {s2}")
print(f"Union: {union_s}")
print("-" * 50)

# ASSIGNMENT QUESTIONS
# ===================

# Question 1: Create a set of first 10 natural numbers
print("Question 1: Create a set of first 10 natural numbers")
s = set(range(1,11))
print(s)

# Question 2: Add element 11 to set {1, 2, 3, 4, 5}
print("\nQuestion 2: Add element 11 to set {1, 2, 3, 4, 5}")
s = {1,2,3,4,5}
s.add(11)
print(s)

# Question 3: Remove element 3 from set {1, 2, 3, 4, 5, 6}
print("\nQuestion 3: Remove element 3 from set {1, 2, 3, 4, 5, 6}")
s = {1,2,3,4,5,6}
s.remove(3)
print(s)

# Question 4: Find the intersection of {1, 2, 3, 4, 5} and {4, 5, 6, 7, 8}
print("\nQuestion 4: Find the intersection of {1, 2, 3, 4, 5} and {4, 5, 6, 7, 8}")
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
inter = s1.intersection(s2)
print(inter)

# Question 5: Find the difference between {1, 2, 3, 4, 5} and {4, 5, 6, 7, 8}
print("\nQuestion 5: Find the difference between {1, 2, 3, 4, 5} and {4, 5, 6, 7, 8}")
diff = s1.difference(s2)
print(diff)

# Question 6: Check if 5 is in set {1, 2, 3, 4, 6, 7, 8}
print("\nQuestion 6: Check if 5 is in set {1, 2, 3, 4, 6, 7, 8}")
s = {1,2,3,4,6,7,8}
print(5 in s)

# Question 7: Find the length of set {'a', 'b', 'c', 'd', 'e'}
print("\nQuestion 7: Find the length of set {'a', 'b', 'c', 'd', 'e'}")
s = {'a','b','c','d','e'}
print(len(s))

# Question 8: Create a set of vowels from string "hello world"
print("\nQuestion 8: Create a set of vowels from string 'hello world'")
s = set(c for c in "hello world" if c in 'aeiou')
print(s)

# Question 9: Remove duplicates from list [1, 2, 2, 3, 4, 4, 5, 6, 6, 7] using set
print("\nQuestion 9: Remove duplicates from list [1, 2, 2, 3, 4, 4, 5, 6, 6, 7] using set")
lst = [1,2,2,3,4,4,5,6,6,7]
s = set(lst)
print(s)

# Question 10: Check if {1, 2, 3} is a subset of {1, 2, 3, 4, 5, 6}
print("\nQuestion 10: Check if {1, 2, 3} is a subset of {1, 2, 3, 4, 5, 6}")
s1 = {1,2,3}
s2 = {1,2,3,4,5,6}
print(s1.issubset(s2))
