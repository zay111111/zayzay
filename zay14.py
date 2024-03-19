import random

print(input("Choose bwtween 1 and 2 : "))
coin = random.randint(1,2)
if coin == 1:
    print("Heads")
if coin == 2:
    print("Tails")

