# Write a program that takes a value in meters and converts it to centimeters and millimeters

meterValue = int(input('Insira um valor em metros: '))

centimeterValue = meterValue * 100
milimeterValue = meterValue * 1000

print(f'O valor em centímetros é igual a: {centimeterValue} \nO valor em milímetros é igual a: {milimeterValue}')
