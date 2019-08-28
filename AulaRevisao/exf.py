area = float(input("Qual o tamanho em metros quadrados da área a ser pintada? "))

litrosUsados = area / 3
custo = litrosUsados * 80

print("Custará R$", float("{0:.2f}".format(custo)), " reais")

