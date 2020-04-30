# -*- coding: utf-8 -*-
"""

basic calc

"""

from colorama import  Fore, Back,Style

operator = input("What do you want to do? (+, -, *, / : ")

a = float( input("Enter the first number: "))
b = float( input("Enter the second number: "))

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

