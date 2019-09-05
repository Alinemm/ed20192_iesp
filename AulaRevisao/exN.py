def main():
   soma = 0
   for tmp in range(1,6):
       tempo = int(input("tempo "+str(tmp)+": "))
       soma = soma + tempo

   print("tempo médio de espera: ", int(soma/5)," minutos")

main()