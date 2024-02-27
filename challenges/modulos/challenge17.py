# Make a program that reads the length of the opposite and adjacent sides of a right triangle, calculates and displays the length of the hypotenuse.

catetoOposto = float(input("Insira o valor do cateto oposto: "))
catetoAdjacente = float(input("Insira o valor do cateto adjacente: "))

hipotenusa = (catetoOposto**2 + catetoAdjacente**2) ** (1/2)

print(f"A hipotenusa de um triângulo com catetos de valor {catetoOposto} e {catetoAdjacente} é igual a {hipotenusa:.2f}")
