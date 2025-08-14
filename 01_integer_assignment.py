# INTEGER DATATYPE ASSIGNMENT
# ===========================

# SOLVED EXAMPLE
# --------------
# Question: Calculate the sum of first 5 even numbers
print("SOLVED EXAMPLE:")
print("Calculate the sum of first 5 even numbers")
first_5_even = [2, 4, 6, 8, 10]
sum_even = sum(first_5_even)
print(f"First 5 even numbers: {first_5_even}")
print(f"Sum: {sum_even}")
print("-" * 50)

# ASSIGNMENT QUESTIONS
# ===================

# Question 1: Calculate the product of first 10 natural numbers
print("Question 1: Calculate the product of first 10 natural numbers")
num = 1
for i in range(1, 11):
    num = num * i
print(num)

# Question 2: Find the remainder when 156 is divided by 7
print("\nQuestion 2: Find the remainder when 156 is divided by 7")
rem = 156 % 7
print(f"\n The remainder when 156 is divided by 7 is {rem}")

# Question 3: Calculate the square of 25
print("\nQuestion 3: Calculate the square of 25")
square = 25 * 25
print(f" The square of 25 is {square}")

# Question 4: Find the cube root of 125
print("\nQuestion 4: Find the cube root of 125")
cb = 125**(1/3)
print(f" The cube root of 125 is {cb}")

# Question 5: Calculate the sum of digits in number 12345
print("\nQuestion 5: Calculate the sum of digits in number 12345")
num = 12345
sum = 0
for i in str(num):
    sum += int(i)
print(f"the sum of the digits 12345 is {sum}")

# Question 6: Check if 97 is a prime number
print("\nQuestion 6: Check if 97 is a prime number")
num = 97
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")

# Question 7: Find the factorial of 8
print("\nQuestion 7: Find the factorial of 8")
num = 8
fact = 1
for i in range(1,num+1):
    fact *= i
print(f"The factorial of {num} is {fact} ")

# Question 8: Calculate the average of numbers: 15, 23, 31, 42, 56
print("\nQuestion 8: Calculate the average of numbers: 15, 23, 31, 42, 56")
num = 15,23,31,42,56
avg = sum(num)/len(num)
print(f"The average of the numbers is {avg}")

# Question 9: Find the greatest common divisor (GCD) of 48 and 36
print("\nQuestion 9: Find the greatest common divisor (GCD) of 48 and 36")
import math
a = 48
b = 36
gcd = math.gcd(a,b)
print(f"The GCD of {a} and {b} is {gcd}")

# Question 10: Calculate the sum of first 20 odd numbers
print("\nQuestion 10: Calculate the sum of first 20 odd numbers")
num = 20
sum = 0
for i in range(1,num*2,2):
    sum += i
print(f"The sum of first {num} odd numbers is {sum} ")
