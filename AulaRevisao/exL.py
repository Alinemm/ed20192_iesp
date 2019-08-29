def main():
   precoProd1 = float(input("Preço do produto 1: "))
   precoProd2 = float(input("Preço do produto 2: "))
   precoProd3 = float(input("Preço do produto 3: "))

   if (precoProd1 < precoProd2 and precoProd1 < precoProd3):
       print("O produto 1 é o mais barato!")
   elif(precoProd2 < precoProd1 and precoProd2 < precoProd3):
       print("O produto 2 é o mais barato!")
   elif (precoProd3 < precoProd1 and precoProd3 < precoProd2):
       print("O produto 3 é o mais barato!")

main()