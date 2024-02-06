# Write a program that takes a value in meters and converts it to centimeters and millimeters

meterValue = float(input('Insira um valor em metros: '))

kilometerValue = meterValue / 1000
hectometerValue = meterValue / 100
decameterValue = meterValue / 10
decimeterValue = meterValue * 10
centimeterValue = meterValue * 100
milimeterValue = meterValue * 1000

print(f'As conversões para {meterValue}m são:')
print(f'{kilometerValue}km')
print(f'{hectometerValue}hm')
print(f'{decameterValue}dam')
print(f'{decimeterValue}dm')
print(f'{centimeterValue}cm')
print(f'{milimeterValue}mm')
