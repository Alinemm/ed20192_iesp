def main():
   nota1 = float(input("digite a nota 1: "))
   nota2 = float(input("digite a nota 2: "))

   media =  (nota1 + nota2)/ 2

   if (media < 7):
       print("Reprovado !")
   elif(media == 10):
       print("Aprovado com distinção!")
   else:
       print("Aprovado")

main()