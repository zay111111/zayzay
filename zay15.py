import random

choice = int(input("Choose bwtween 1 and 2 : "))
coin = random.randint(1,2)
if coin == 1:
    print("Heads")
if coin == 2:
    print("Tails")

if choice == 1 and coin == 1:
    print("Tw dl kg ly! ")
elif choice == 2 and coin == 1:
    print("Sorry kwr " )
if choice == 2 and coin == 2:
    print("Tw dl kg ly! ")
elif choice == 1 and coin == 2:
    print("Sorry kwr " )