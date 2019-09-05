def main():
   p1 = float(input("Informe o preço do prod 1:"))
   p2 = float(input("Informe o preço do prod 2:"))
   p3 = float(input("Informe o preço do prod 3:"))

   if p1 < p2 and p1 < p3:
       print("P1 é o mais barato")
   elif p2< p1 and p2 < p3:
       print("P2 é o mais barato")
   else:
       print("P3 é o mais barato")

main()
