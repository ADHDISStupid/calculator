import os
import time
from pyfiglet import Figlet

FONT = Figlet(font='slant')

def clear_screen():
    print("Restarting in 10 seconds...")
    time.sleep(10)
    os.system('cls' if os.name == 'nt' else 'clear')

def int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Sorry, only integers accepted, try again.")

while True:
    print(FONT.renderText("Calculator"))

    number = int_input("Number1: ")
    number2 = int_input("Number2: ")
    opt = input("+, -, *, / (or q to quit): ")

    match opt:
        case 'q':
            print("Goodbye!")
            break

        case '+':
            result = number + number2
            print(f"Result: {result}")
            clear_screen()

        case '-':
            result = number - number2
            print(f"Result: {result}")
            clear_screen()

        case '*':
            result = number * number2
            print(f"Result: {result}")
            clear_screen()

        case '/':
            if number2 == 0:
                print("Cannot divide by 0")
            else:
                result = number / number2
                print(f"Result: {result}")
            clear_screen()

        case _:
            print("Not an allowed operation")
            clear_screen()
