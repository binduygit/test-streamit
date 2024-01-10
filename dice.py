from random import randint

num_dice = int(input("how many dice are you rolling? "))
num_sides= int(input("how many sides on each dice? "))

while True:
    result = '|'
    for die in range(num_dice):
        rand = randint(1, num_sides)
        result += str(rand) + "|"
    print(result)
    reply = input("Roll again ? (q for quit)")
    if(reply == 'q'):
        break
