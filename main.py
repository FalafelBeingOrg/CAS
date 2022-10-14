from sympy import *


a = "**"
newPower = "^"
out = ""

x, y, z = symbols('x y z')
init_printing(use_unicode=True)

choice = input('s: simplify, f: factor, e: expand, co: collect, ca: cancel> ')
if choice == 's':
    text = input("Enter an expression to be simplified> ")
    print(simplify(text))

if choice == 'f':
    text = input("Enter an expression to be factored> ")
    print(factor(text))

if choice == 'e':
    text = input("Enter an expression to be expanded> ")
    print(expand(text))

if choice == 'co':
    text = input("Enter an expression to be collected> ")
    print(collect(text))

if choice == 'ca':
    text = input("Enter an expression to be canceled> ")
    print(cancel(text))
