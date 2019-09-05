def main():
   gen = input("Digite o gênero: ")

   if (gen == 'F' or gen == 'f'):
       print("F - feminino")
   elif(gen == 'M' or gen == 'm'):
       print("M - masculino")
   else:
       print("Gênero inválido")

main()