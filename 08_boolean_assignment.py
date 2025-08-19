# BOOLEAN DATATYPE ASSIGNMENT
# ==========================

# SOLVED EXAMPLE
# --------------
# Question: Check if a number is both even and greater than 10
print("SOLVED EXAMPLE:")
print("Check if a number is both even and greater than 10")
number = 16
is_even = number % 2 == 0
is_greater_than_10 = number > 10
result = is_even and is_greater_than_10
print(f"Number: {number}")
print(f"Is even: {is_even}")
print(f"Is greater than 10: {is_greater_than_10}")
print(f"Both conditions: {result}")
print("-" * 50)

# ASSIGNMENT QUESTIONS
# ===================

# Question 1: Check if 25 is greater than 20 and less than 30
print("Question 1: Check if 25 is greater than 20 and less than 30")
number = 25
result = number > 20 and number < 30
print(result)

# Question 2: Check if string "python" is equal to "Python" (case sensitive)
print("\nQuestion 2: Check if string 'python' is equal to 'Python' (case sensitive)")
result = "python" == "Python"
print(result)

# Question 3: Check if 15 is divisible by both 3 and 5
print("\nQuestion 3: Check if 15 is divisible by both 3 and 5")
number = 15
result = number % 3 == 0 and number % 5 == 0
print(result)

# Question 4: Check if 7 is not equal to 8
print("\nQuestion 4: Check if 7 is not equal to 8")
result = 7 != 8
print(result)

# Question 5: Check if 100 is greater than 50 or less than 25
print("\nQuestion 5: Check if 100 is greater than 50 or less than 25")
number = 100
result = number > 50 or number < 25
print(result)

# Question 6: Check if 0 is falsy in Python
print("\nQuestion 6: Check if 0 is falsy in Python")
result = bool(0)
print(result)

# Question 7: Check if empty string "" is falsy in Python
print("\nQuestion 7: Check if empty string '' is falsy in Python")
result = bool("")
print(result)

# Question 8: Check if 42 is truthy in Python
print("\nQuestion 8: Check if 42 is truthy in Python")
result = bool(42)
print(result)

# Question 9: Check if 10 is between 5 and 15 (inclusive)
print("\nQuestion 9: Check if 10 is between 5 and 15 (inclusive)")
number = 10
result = 5 <= number <= 15
print(result)

# Question 10: Check if 3.14 is greater than 3 and less than 4
print("\nQuestion 10: Check if 3.14 is greater than 3 and less than 4")
number = 3.14
result = number > 3 and number < 4
print(result)
