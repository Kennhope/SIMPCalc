import math


def add(x,y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    return x / y

def exp(x,y):
    return x ** y

def sqrt(x):
    math.sqrt(x)



print("Welcome to the SIMP Calc bEtA 1.0")
print ("What do you want to do? :)")
print ("+ Add")
print ("- Subtract")
print ("* Multiply")
print ("/ Divide")
print ("^ Exponentiation")
print ("sqrt. Square Root")


while True:
    choice = input("Enter your choice(sign): ")


    if choice in ('+', '-', '*', '/', '^'):
        num1 = float(input("Enter your first number in here: "))
        num2 = float(input("And another number in here: "))
    elif choice in ('sqrt'):
        num1 = float(input("Which number you want to calculate? : "))



        if choice == '+':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '-':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '*':
            print(num1, "x", num2, "=", multiply(num1, num2))

        elif choice == '/':
            print(num1, "/", num2, "=", divide(num1, num2))
            break

        elif choice == '^':
            print(num1, "^", num2, "=", exp(num1, num2))

        elif choice == 'sqrt':
             print("√", num1, "=", math.sqrt(num1))




    else:
            print("Sorry, there is no function like that :(")
