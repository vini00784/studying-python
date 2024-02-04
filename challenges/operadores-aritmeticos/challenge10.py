# Write a program that reads the amount of money a person has and how many dollars they can buy
# US$1 = R$3.27

value = float(input('Insira quanto você tem na conta: '))

dollars = value / 3.27

print(f'Você tem {value} na carteira e pode comprar {dollars:.2f} dólares')
