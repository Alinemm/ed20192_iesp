#Dado um inteiro não-negativo n, determinar n!

def main1():
   numero =  int(input("Digite um número inteiro positivo: "))
   fatorial = 1

   if (numero>0):
       for n in range(1, numero+1):
           print(n)
           fatorial = fatorial * n
   print(numero,"! = ",fatorial)

def main2():
   numero =  int(input("Digite um número inteiro positivo: "))
   fatorial = 1

   if(numero>0):
       n = 1
       while(n <= numero):
           print(n)
           fatorial = fatorial * n
           n = n + 1
   print(numero, "! = ", fatorial)

main1()
main2()

#Dado um inteiro não-negativo n, determinar n!

def main1():
   numero =  int(input("Digite um número inteiro positivo: "))
   fatorial = 1

   if (numero>0):
       for n in range(1, numero+1):
           #print(n)
           fatorial = fatorial * n
   print(numero,"! = ",fatorial)

def main2():
   numero =  int(input("Digite um número inteiro positivo: "))
   fatorial = 1

   if(numero>0):
       n = 1
       while(n <= numero):
           #print(n)
           fatorial = fatorial * n
           n = n + 1
   print(numero, "! = ", fatorial)

main1()
main2()