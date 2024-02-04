# Write a program that reads the width and height of a wall, calculates its area and the amount of paint needed to paint, it knowing that each liter paints an area of 2m²

wallWidth = float(input('Qual a largura da sua parede (em metros)? '))
wallHeight = float(input('Qual a altura da sua parede (em metros)? '))

wallArea = wallWidth * wallHeight
paintQuantity = wallArea / 2

print(f'A área da sua parede é igual a {wallArea} \nE a quantidade de tinta necessária para pintar essa parede é de {paintQuantity} litros')