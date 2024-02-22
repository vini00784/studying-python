# Make a program that reads any angle and shows the value of sine, cosine and tangent on the screen

from math import cos, sin, tan, radians

angle = int(input("Insira o valor de um ângulo qualquer: "))

sine = sin(radians(angle))
cosine = cos(radians(angle))
tangent = tan(radians(angle))

print(f"Sobre o ângulo {angle}:")
print(f"O seno é igual a {sine:.2f}")
print(f"O cosseno é igual a {cosine:.2f}")
print(f"A tangente é igual a {tangent:.2f}")
