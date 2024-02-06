# Write a program that reads the amount of money a person has and how many dollars they can buy
# US$1 = R$3.27
# 1 EUR = R$5.35
# 1 GBP = R$6.25 

value = float(input('Insira quanto você tem na conta: R$'))

dollars = value / 3.27
euros = value / 5.35
pounds = value / 6.25

print(f'Você tem R${value} na carteira e pode comprar:')
print(f'US${dollars:.2f}')
print(f'{euros:.2f} euros')
print(f'{pounds:.2f} pounds')
