# Write a program that reads the amount of money a person has and how many dollars they can buy
# US$1 = R$3.27

value = float(input('Insira quanto você tem na conta: R$'))

dollars = value / 3.27

print(f'Você tem R${value} na carteira e pode comprar US${dollars:.2f}')
