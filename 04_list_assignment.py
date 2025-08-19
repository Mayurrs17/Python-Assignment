# LIST DATATYPE ASSIGNMENT - 50 QUESTIONS
# ======================================

# SOLVED EXAMPLE
# --------------
# Question: Find the maximum and minimum values in a list
print("SOLVED EXAMPLE:")
print("Find the maximum and minimum values in a list")
lst = [23, 45, 12, 67, 34, 89, 56]
mx = max(lst)
mn = min(lst)
print(f"List: {lst}")
print(f"Maximum: {mx}")
print(f"Minimum: {mn}")
print("-" * 50)

# ASSIGNMENT QUESTIONS (50 QUESTIONS)
# ==================================

# Question 1: Create a list of first 10 square numbers
print("Question 1: Create a list of first 10 square numbers")
lst = [i**2 for i in range(1, 11)]
print(lst)

# Question 2: Find the sum of all even numbers in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("\nQuestion 2: Find the sum of all even numbers in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]")
lst = list(range(1, 11))
s = sum(i for i in lst if i%2==0)
print(s)

# Question 3: Remove duplicates from [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
print("\nQuestion 3: Remove duplicates from [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]")
lst = [1,2,2,3,4,4,5,6,6,7]
lst = list(set(lst))
print(lst)

# Question 4: Sort the list [64, 34, 25, 12, 22, 11, 90] in descending order
print("\nQuestion 4: Sort the list [64, 34, 25, 12, 22, 11, 90] in descending order")
lst = [64,34,25,12,22,11,90]
lst.sort(reverse=True)
print(lst)

# Question 5: Find the average of numbers in [15, 23, 31, 42, 56, 78, 91]
print("\nQuestion 5: Find the average of numbers in [15, 23, 31, 42, 56, 78, 91]")
lst = [15,23,31,42,56,78,91]
avg = sum(lst)/len(lst)
print(avg)

# Question 6: Create a list of first 15 Fibonacci numbers
print("\nQuestion 6: Create a list of first 15 Fibonacci numbers")
lst = [0,1]
for i in range(2,15):
    lst.append(lst[i-1]+lst[i-2])
print(lst)

# Question 7: Find the second largest number in [45, 67, 23, 89, 12, 34, 78]
print("\nQuestion 7: Find the second largest number in [45, 67, 23, 89, 12, 34, 78]")
lst = [45,67,23,89,12,34,78]
lst.sort(reverse=True)
print(lst[1])

# Question 8: Reverse the list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("\nQuestion 8: Reverse the list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]")
lst = list(range(1,11))
lst.reverse()
print(lst)

# Question 9: Count how many times 5 appears in [1, 5, 2, 5, 3, 5, 4, 5, 6]
print("\nQuestion 9: Count how many times 5 appears in [1, 5, 2, 5, 3, 5, 4, 5, 6]")
lst = [1,5,2,5,3,5,4,5,6]
print(lst.count(5))

# Question 10: Create a list of prime numbers between 1 and 50
print("\nQuestion 10: Create a list of prime numbers between 1 and 50")
primes = []
for i in range(2,51):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        primes.append(i)
print(primes)

# Question 11: Flatten nested list [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("\nQuestion 11: Flatten nested list [[1, 2, 3], [4, 5, 6], [7, 8, 9]]")
lst = [[1,2,3],[4,5,6],[7,8,9]]
flat = [i for sub in lst for i in sub]
print(flat)

# Question 12: Find common elements between [1, 2, 3, 4, 5] and [4, 5, 6, 7, 8]
print("\nQuestion 12: Find common elements between [1, 2, 3, 4, 5] and [4, 5, 6, 7, 8]")
a = [1,2,3,4,5]
b = [4,5,6,7,8]
common = [i for i in a if i in b]
print(common)

# Question 13: Create a list of lists: [[1, 2], [3, 4], [5, 6]]
print("\nQuestion 13: Create a list of lists: [[1, 2], [3, 4], [5, 6]]")
lst = [[1,2],[3,4],[5,6]]
print(lst)

# Question 14: Find the sum of each sublist in [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("\nQuestion 14: Find the sum of each sublist in [[1, 2, 3], [4, 5, 6], [7, 8, 9]]")
lst = [[1,2,3],[4,5,6],[7,8,9]]
sums = [sum(sub) for sub in lst]
print(sums)

# Question 15: Transpose the matrix [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("\nQuestion 15: Transpose the matrix [[1, 2, 3], [4, 5, 6], [7, 8, 9]]")
mat = [[1,2,3],[4,5,6],[7,8,9]]
trans = [[row[i] for row in mat] for i in range(len(mat[0]))]
print(trans)

# Question 16: Find the maximum value in each sublist of [[1, 5, 3], [9, 2, 7], [4, 8, 6]]
print("\nQuestion 16: Find the maximum value in each sublist of [[1, 5, 3], [9, 2, 7], [4, 8, 6]]")
lst = [[1,5,3],[9,2,7],[4,8,6]]
mx = [max(sub) for sub in lst]
print(mx)

# Question 17: Create a 3D list: [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
print("\nQuestion 17: Create a 3D list: [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]")
lst = [[[1,2],[3,4]],[[5,6],[7,8]]]
print(lst)

# Question 18: Find the sum of all elements in 3D list [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
print("\nQuestion 18: Find the sum of all elements in 3D list [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]")
lst = [[[1,2],[3,4]],[[5,6],[7,8]]]
total = sum(i for sub1 in lst for sub2 in sub1 for i in sub2)
print(total)

# Question 19: Extract all even numbers from nested list [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("\nQuestion 19: Extract all even numbers from nested list [[1, 2, 3], [4, 5, 6], [7, 8, 9]]")
lst = [[1,2,3],[4,5,6],[7,8,9]]
evens = [i for sub in lst for i in sub if i%2==0]
print(evens)

# Question 20: Create a list of mixed data types: [1, "hello", 3.14, True, [1, 2, 3]]
print("\nQuestion 20: Create a list of mixed data types: [1, 'hello', 3.14, True, [1, 2, 3]]")
lst = [1,"hello",3.14,True,[1,2,3]]
print(lst)

# Question 21: Find the length of each string in ["apple", "banana", "cherry", "date"]
print("\nQuestion 21: Find the length of each string in ['apple', 'banana', 'cherry', 'date']")
lst = ["apple","banana","cherry","date"]
lens = [len(i) for i in lst]
print(lens)

# Question 22: Create a list of tuples: [(1, 'a'), (2, 'b'), (3, 'c')]
print("\nQuestion 22: Create a list of tuples: [(1, 'a'), (2, 'b'), (3, 'c')]")
lst = [(1,'a'),(2,'b'),(3,'c')]
print(lst)

# Question 23: Extract first element from each tuple in [(1, 'a'), (2, 'b'), (3, 'c')]
print("\nQuestion 23: Extract first element from each tuple in [(1, 'a'), (2, 'b'), (3, 'c')]")
lst = [(1,'a'),(2,'b'),(3,'c')]
first = [i[0] for i in lst]
print(first)

# Question 24: Create a list of dictionaries: [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}]
print("\nQuestion 24: Create a list of dictionaries: [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}]")
lst = [{'name':'Alice','age':25},{'name':'Bob','age':30}]
print(lst)

# Question 25: Extract all 'name' values from list of dictionaries
print("\nQuestion 25: Extract all 'name' values from list of dictionaries")
names = [i['name'] for i in lst]
print(names)

# Question 26: Find the person with maximum age in list of dictionaries
print("\nQuestion 26: Find the person with maximum age in list of dictionaries")
oldest = max(lst, key=lambda x: x['age'])
print(oldest)

# Question 27: Create a 4D list: [[[[1, 2], [3, 4]], [[5, 6], [7, 8]]], [[[9, 10], [11, 12]], [[13, 14], [15, 16]]]]
print("\nQuestion 27: Create a 4D list: [[[[1, 2], [3, 4]], [[5, 6], [7, 8]]], [[[9, 10], [11, 12]], [[13, 14], [15, 16]]]]")
lst = [[[[1,2],[3,4]],[[5,6],[7,8]]],[[[9,10],[11,12]],[[13,14],[15,16]]]]
print(lst)

# Question 28: Find the maximum value in 4D list
print("\nQuestion 28: Find the maximum value in 4D list")
mx = max(i for l1 in lst for l2 in l1 for l3 in l2 for i in l3)
print(mx)

# Question 29: Create a list of sets: [{1, 2, 3}, {4, 5, 6}, {7, 8, 9}]
print("\nQuestion 29: Create a list of sets: [{1, 2, 3}, {4, 5, 6}, {7, 8, 9}]")
lst = [{1,2,3},{4,5,6},{7,8,9}]
print(lst)

# Question 30: Find the union of all sets in list of sets
print("\nQuestion 30: Find the union of all sets in list of sets")
uni = set().union(*lst)
print(uni)

# Question 31: Create a list of complex numbers: [1+2j, 3+4j, 5+6j]
print("\nQuestion 31: Create a list of complex numbers: [1+2j, 3+4j, 5+6j]")
lst = [1+2j,3+4j,5+6j]
print(lst)

# Question 32: Find the magnitude of each complex number in list
print("\nQuestion 32: Find the magnitude of each complex number in list")
mag = [abs(i) for i in lst]
print(mag)

# Question 33: Create a nested list with different levels: [1, [2, 3], [4, [5, 6]], 7]
print("\nQuestion 33: Create a nested list with different levels: [1, [2, 3], [4, [5, 6]], 7]")
lst = [1,[2,3],[4,[5,6]],7]
print(lst)

# Question 34: Count the depth of nesting in [1, [2, 3], [4, [5, 6]], 7]
print("\nQuestion 34: Count the depth of nesting in [1, [2, 3], [4, [5, 6]], 7]")
def depth(lst):
    if isinstance(lst,list):
        return 1 + max((depth(i) for i in lst), default=0)
    else:
        return 0
print(depth(lst))

# Question 35: Create a list of functions: [len, str, int, float]
print("\nQuestion 35: Create a list of functions: [len, str, int, float]")
funcs = [len,str,int,float]
print(funcs)

# Question 36: Apply each function in list to string "123"
print("\nQuestion 36: Apply each function in list to string '123'")
results = [f("123") for f in funcs]
print(results)

# Question 37: Create a list of lambda functions: [lambda x: x*2, lambda x: x**2, lambda x: x+1]
print("\nQuestion 37: Create a list of lambda functions: [lambda x: x*2, lambda x: x**2, lambda x: x+1]")
lambdas = [lambda x:x*2, lambda x:x**2, lambda x:x+1]
print(lambdas)

# Question 38: Apply each lambda function to 5
print("\nQuestion 38: Apply each lambda function to 5")
res = [f(5) for f in lambdas]
print(res)

# Question 39: Create a list of classes: [list, dict, set, tuple]
print("\nQuestion 39: Create a list of classes: [list, dict, set, tuple]")
classes = [list,dict,set,tuple]
print(classes)

# Question 40: Create instances of each class in list
print("\nQuestion 40: Create instances of each class in list")
instances = [c() for c in classes]
print(instances)

# Question 41: Create a list of None values: [None, None, None, None]
print("\nQuestion 41: Create a list of None values: [None, None, None, None]")
lst = [None]*4
print(lst)

# Question 42: Replace all None values with 0 in list
print("\nQuestion 42: Replace all None values with 0 in list")
lst = [0 if i is None else i for i in lst]
print(lst)

# Question 43: Create a list of boolean values: [True, False, True, False]
print("\nQuestion 43: Create a list of boolean values: [True, False, True, False]")
lst = [True,False,True,False]
print(lst)

# Question 44: Count True values in boolean list
print("\nQuestion 44: Count True values in boolean list")
print(lst.count(True))

# Question 45: Create a list of ranges: [range(3), range(5), range(2)]
print("\nQuestion 45: Create a list of ranges: [range(3), range(5), range(2)]")
lst = [range(3),range(5),range(2)]
print(lst)

# Question 46: Convert each range to list
print("\nQuestion 46: Convert each range to list")
lst = [list(r) for r in lst]
print(lst)

# Question 47: Create a list of generators: [(x for x in range(3)), (x for x in range(5))]
print("\nQuestion 47: Create a list of generators: [(x for x in range(3)), (x for x in range(5))]")
gens = [(x for x in range(3)),(x for x in range(5))]
print(gens)

# Question 48: Convert each generator to list
print("\nQuestion 48: Convert each generator to list")
lists = [list(g) for g in gens]
print(lists)

# Question 49: Create a list of iterators: [iter([1, 2, 3]), iter([4, 5, 6])]
print("\nQuestion 49: Create a list of iterators: [iter([1, 2, 3]), iter([4, 5, 6])]")
iters = [iter([1,2,3]), iter([4,5,6])]
print(iters)

# Question 50: Extract all elements from each iterator
print("\nQuestion 50: Extract all elements from each iterator")
lists = [list(it) for it in iters]
print(lists)
