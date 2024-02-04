n1 = int(input('Insira um valor: '))
n2 = int(input('Insira outro valor: '))

sumValue = n1 + n2
subValue = n1 - n2
mulValue = n1 * n2
divValue = n1 / n2
entDivValue = n1 // n1
expoValue = n1 ** n2

print(f'A soma é igual a {sumValue} \nA subtração é igual a {subValue} \nA multiplicação é igual a {mulValue} \nA divisão é igual a {divValue:.3f} \nA divisão inteira é igual a {entDivValue} \nA exponenciação é igual a {expoValue}')