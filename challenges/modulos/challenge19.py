# A teacher wants to draw one of his four students to erase the board. Make a program that helps him, reading their name and writing the name of the chosen one

import random

student1 = input("Insira o nome do primeiro aluno: ")
student2 = input("Insira o nome do segundo aluno: ")
student3 = input("Insira o nome do terceiro aluno: ")
student4 = input("Insira o nome do quarto aluno: ")

print(f"Aluno 1: {student1}")
print(f"Aluno 2: {student2}")
print(f"Aluno 3: {student3}")
print(f"Aluno 4: {student4}")

array_students = [student1, student2, student3, student4]

drawnStudent = random.choice(array_students)

print(f"O aluno sorteado foi o(a): {drawnStudent}")
