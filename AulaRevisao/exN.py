def main():
   numNotas = int(input("Quantas notas você quer armazenar? "))

   soma = 0
   for x in range(0, numNotas):
       nota = float(input("Nota "+ str(x) + ": "))
       soma = soma + nota
   media = soma / numNotas

   print("média: "+ str(media))

main()