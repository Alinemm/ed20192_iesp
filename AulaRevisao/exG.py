def main():
   numInt1 = int(input("Digite um número inteiro: "))
   numInt2 = int(input("Digite outro número inteiro: "))
   numReal = float(input("Digite um número real: "))

   op1 = (2* numInt1) * (numInt2 /2)
   op2 = (3* numInt1) + numInt2
   op3 = numReal ** 3

   print(" o produto do dobro do primeiro com metade do segundo é: " + str(op1))
   print(" a soma do triplo do primeiro com o terceiro é: " + str(op2))
   print(" o terceiro elevado ao cubo é: " + str(op3))

main()

