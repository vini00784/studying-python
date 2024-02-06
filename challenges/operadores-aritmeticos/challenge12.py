# Make a program that reads a product price and displays a new price with 5% of discount

price = float(input('Insira o valor do produto: R$'))

priceWithDiscount = price - price * 0.05

print(f'O valor original do produto é: R${price} \nCom um desconto de 5% fica: R${priceWithDiscount}')
