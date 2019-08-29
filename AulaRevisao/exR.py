def main1():
   nome = input("digite uma palavra: ")

   nomeTmp = nome.casefold()
   inverso = reversed(nomeTmp)

   if list(nome) == list(inverso):
       print("É um palíndromo!")
   else:
       print("Não é um palíndromo!")

def main2():
   nome = input("digite uma palavra: ")
   inverso = ""
   tam = len(nome) -1

   for i in range(tam, -1, -1):
       inverso = inverso + nome[i]

   if(nome == inverso):
       print(nome, " e ",inverso, " são palíndromos!")
   else:
       print(nome, " e ", inverso, " não são palíndromos!")

main1()
main2()