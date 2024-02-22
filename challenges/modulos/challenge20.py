# The same teacher from the previous challenge will draw the order in which the students will present. Make a program that reads the names of the four students and shows the order drawn.

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

random.shuffle(array_students) # There is no return, so there is no need to store it in a variable

print(f"A ordem sorteada foi: {array_students}")
