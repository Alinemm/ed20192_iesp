def main():
   maior = -1000000
   for n in range(0,3):
       num = float(input("Digite um número: "))
       if(maior < num):
           maior = num

   print("O maior valor é: "+ str(maior))

main()