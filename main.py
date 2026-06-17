import os
import time
import pyfiglet
from pyfiglet import Figlet

FONT = Figlet(font='slant')

def clear_screen():
    print("Restarting in 10 secounds")
    time.sleep(10)
    os.system('cls')


while (True):
    try:
        print(FONT.renderText("Calculator"))
        number = int(input("number 1: "))
        number2 = int(input("number 2: "))
        opt = input("+, -, *, /: ")
    except:
        print("invalid number.")
        continue

    if opt == "q":
        print("goodbye")
        break

    match opt:
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
            if number2 != 0:
                result = number / number2
                print(f"Result: {result}")
                clear_screen()
            else:
                print("Cannot david by 0") 
                clear_screen()
        case _:
            print("Not a OPT")
            clear_screen()
