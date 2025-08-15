# FLOAT DATATYPE ASSIGNMENT
# =========================

# SOLVED EXAMPLE
# --------------
# Question: Calculate the area of a circle with radius 5.5
print("SOLVED EXAMPLE:")
print("Calculate the area of a circle with radius 5.5")
import math
radius = 5.5
area = math.pi * radius ** 2
print(f"Radius: {radius}")
print(f"Area: {area:.2f}")
print("-" * 50)

# ASSIGNMENT QUESTIONS
# ===================

# Question 1: Calculate the average of 3.14, 2.718, 1.618, 0.577
print("Question 1: Calculate the average of 3.14, 2.718, 1.618, 0.577")
nums = [3.14, 2.718, 1.618, 0.577]
avg = sum(nums) / len(nums)
print(f"The average of the numbers is {avg:.4f}")

# Question 2: Convert 98.6 Fahrenheit to Celsius (F = C * 9/5 + 32)
print("\nQuestion 2: Convert 98.6 Fahrenheit to Celsius")
fahrenheit = 98.6
celcius = (f - 32) * 5/9
print(celcius)

# Question 3: Calculate the compound interest on $1000 at 5.5% for 3 years
print("\nQuestion 3: Calculate compound interest on $1000 at 5.5% for 3 years")
p = 1000
r = 5.5 / 100
t = 3
ci = p * ((1 + r) ** t) - p
print(f"Compound Interest after {t} years is: {ci:.2f}")

# Question 4: Find the hypotenuse of a right triangle with sides 3.5 and 4.2
print("\nQuestion 4: Find the hypotenuse of a right triangle with sides 3.5 and 4.2")
a = 3.5
b = 4.2
hyp = (a**2 + b**2) ** 0.5
print(f"The hypotenuse of a right triangle with sides {a} and {b} is {hyp:.2f}")


# Question 5: Calculate the volume of a sphere with radius 7.8
print("\nQuestion 5: Calculate the volume of a sphere with radius 7.8")
import math
rad = 7.8
vol = (4/3) * math.pi * r**3
print(f"The volume of a sphere with radius {rad} is {vol:.4f}")

# Question 6: Round 3.14159 to 3 decimal places
print("\nQuestion 6: Round 3.14159 to 3 decimal places")
num = 3.14159
print(f"{num:.3f}")

# Question 7: Calculate the percentage: 45 out of 67
print("\nQuestion 7: Calculate the percentage: 45 out of 67")
a = 45
b = 67
percentage = (a/b)*100
print(f"The percentage: 45 out of 67 is {percentage:.2f}%")

# Question 8: Find the square root of 23.456
print("\nQuestion 8: Find the square root of 23.456")
num = 23.456
sr = num**(1/2)
print(f"The square root of 23.456 is {sr:.2f}")

# Question 9: Calculate the simple interest: Principal=2500, Rate=6.5%, Time=2.5 years
print("\nQuestion 9: Calculate simple interest: Principal=2500, Rate=6.5%, Time=2.5 years")
principal = 2500
rate = 6.5
time = 2.5
si = (P * R * T) / 100
print(f"simple intrest is {si:.2f}")

# Question 10: Convert 45.7 degrees to radians
print("\nQuestion 10: Convert 45.7 degrees to radians")
import math
deg = 45.7
rad = deg * math.pi / 180
print(f"{deg} degrees to radians is {rad:.4f}")
