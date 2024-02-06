# Make a program that reads an employee's salary and shows their new salary with a 15% increase

salary = float(input('Qual o seu salário atualmente? '))

salaryWithIncrease = salary + salary * 0.15

print(f'Seu salário atual é R${salary}. \nMas com um aumento de 15% ele vai ficar igual a R${salaryWithIncrease:.2f}, parábens!')
