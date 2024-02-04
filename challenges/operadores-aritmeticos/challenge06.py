# Make an algoritm that reads a number and displays its double, triple ans square root

n = int(input('Escreva um número: '))
double = n * 2
triple = n * 3
squareRoot = n**(1/2)

print(f'Dobro: {double} \nTriplo: {triple} \nRaíz quadrada: {squareRoot:.3f}')