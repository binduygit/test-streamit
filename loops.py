""" import random;
roll1 = random.randint(1,6)
roll2 = random.randint(1,6)
roll_count = 1

while roll1 !=1 or roll2 !=1:
    print(roll1,roll2)
    roll1 = random.randint(1,6)
    roll2 = random.randint(1,6)
    roll_count +=1

print(roll1,roll2)
print(f"YAY SNAKE EYES at count {roll_count}") """

""" for num in range(10,20,4):
  print(num) """

""" for num_bottles in range(99,0,-1):
    print(f"{num_bottles} bottles of beer on the wall")
    print(f"{num_bottles} bottles of beer ")
    if(num_bottles !=1):
        print(f"take one down, pass it around {num_bottles-1} bottles of beer on the wall")
    else:
        print(f"take one down, pass it around no bottles of beer on the wall")
    print("*"*50) """

""" num = 100
while num <=140:
    if num%2 ==0:
        print(num)
    num +=1 """

answer = input("Please say Hi  -");
while True:
    if answer.lower() == 'hi':
        break
    answer = input("Please say Hi -")

print("Hi to you too")