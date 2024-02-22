# Make a program that reads any real number from the keyboard and displays its entire portion on the screen

import math

num = float(input("Digite um número decimal: "))

print(f"A parte inteira desse número é igual a {math.trunc(num)}")
