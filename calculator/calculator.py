print("Hello! This is calculator in Python")
print("Give first number")
num1 = float(input())
print("Give second number")
num2 = float(input())
print("Write one of: + , - , /, *")
calculate = input()


def calculator(number1, number2, calculate1):
    global result
    if calculate1 == "+":
        result = (number1 + number2)

    elif calculate1 == "-":
        result = number1 - number2

    elif calculate1 == "/":
        if number2 != 0:
            result = number1 / number2
        else:
            print("Do not divide by 0")

    elif calculate1 == "*":
        result = number1 * number2

    if result.is_integer():
        print(int(result))
    else:
        print(result)


calculator(num1, num2, calculate)