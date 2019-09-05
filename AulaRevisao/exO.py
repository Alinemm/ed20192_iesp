def main():
   numInicio = int(input("Digite o número de início: "))
   numFim = int(input("Digite o número de fim: "))

   #for tmp in range(numInicio,numFim+1):
   #    print(tmp**2)

   tmp = numInicio
   while(tmp <=numFim):
       print(tmp ** 2)
       tmp = tmp +1

main()