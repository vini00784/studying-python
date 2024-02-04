# Write a program that reads an integer and displays its multiplication table

n = int(input('Digite um número: '))
array_int = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(f'Tabuada do {n}:')

for x in array_int: {
    print(f'{n} x {x} = {n*x}')
}
