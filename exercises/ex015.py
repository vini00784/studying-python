# Write a program that asks the number of km traveled by a rented car and the number of days for which it was rented. Calculate the price to pay, knowing that the car costs R$60 per day and R$0.15 per km driven

km = float(input('Quantos Km você andou com o carro? '))
days = int(input('Por quantos dias você ficou com o carro? '))

price = 60 * days + 0.15 * km

print(f'Você andou {km}km com o carro durante {days} dias. Portanto, o preço a pagar é igual a R${price}')
