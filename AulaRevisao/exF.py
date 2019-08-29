area = float(input("Qual o tamanho em metros quadrados da área a ser pintada? "))

litrosUsados = area/3

if litrosUsados == int( litrosUsados ):
    custo = litrosUsados * 80
else:
    custo = (int(litrosUsados)+1) * 80



print("Custará R$", float("{0:.2f}".format(custo)), " reais")