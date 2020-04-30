# -*- coding: utf-8 -*-
"""

basic calc

"""

operator = input("What do you want to do? (+, -, *, / : ")

a = input("Enter the first number: ")
b = input("Enter the second number: ")

if operator == "+":
    c = a + b
    
elif operator == "-":
    c = a - b
    
elif operator == "*":
    c = a * b

elif operator == "/":
    c = a / b
else:
    print("Error! Incorrect Arithmetic Operator! ")

print ("Result: = " + str(c) )    