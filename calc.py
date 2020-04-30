# -*- coding: utf-8 -*-
"""

basic calc

"""
from colorama import init
from colorama import Fore, Back,Style

# use Colorama to make Termcolor work on Windows too
init()

print(Fore.BLACK)
print(Back.MAGENTA)

operator = input("What do you want to do? (+, -, *, / : ")

print(Back.MAGENTA)

a = float( input("Enter the first number: "))
b = float( input("Enter the second number: "))

print(Back.YELLOW)

if operator == "+":
    c = a + b
    print ("Result: = " + str(c) )
elif operator == "-":
    c = a - b
    print ("Result: = " + str(c) )
elif operator == "*":
    c = a * b
    print ("Result: = " + str(c) )
elif operator == "/":
    c = a / b
    print ("Result: = " + str(c) )
else:
    print("Error! Incorrect Arithmetic Operator! ")

input()