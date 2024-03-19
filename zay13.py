num1 = int(input("Enter Number 1 :"))
num2 = int(input("Enter Number 2 :"))
choice = input("+, -, *, / : ")

if choice == "+":
    answer = num1 + num2
    print("Answer is " + str(answer))

elif choice == "-":
    answer = num1 - num2
    print("Answer is " + str(answer))

elif choice == "*":
    answer = num1 * num2
    print("Answer is " + str(answer))

elif choice == "/":
    answer = num1 / num2
    print("Answer is " + str(answer))

else:
    print("+, -, *, / only accaptable !")