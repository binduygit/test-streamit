numbers = [1, 2, 3, 4, 5]

for num in numbers:
    if num == 3:
        break
    print(num)

 # Exercise 5: Nested loops
for i in range(3):
    for j in range(2):
        print(f"({i}, {j})")

# Exercise 4: Use enumerate to get both index and value
fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

# Exercise 2: Iterate over a string
for char in "Python":
    print(f"Char {char}")

first = "hello   "
first.upper().strip()