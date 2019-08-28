def main():
   salarioHora = float(input("Quanto você ganha por hora? "))
   horasTotal = float(input("Quantas horas por mês você trabalha? "))

   salarioBruto = salarioHora * horasTotal
   print("Salário Bruto: " + str(salarioBruto))

   IPRF = (0.11 * salarioBruto)
   print("valor descontado no IPRF: " + str(IPRF))

   INSS = (0.08 * salarioBruto)
   print("valor descontado no INSS: " + str(INSS))

   sindicato = (0.05 * salarioBruto)
   print("valor descontado no Sindicato: " + str(sindicato))

   salarioLiqui = salarioBruto - INSS - sindicato - IPRF
   print("Salário líquido: " + str(salarioLiqui))

   descontos = INSS + IPRF + sindicato
   print("Descontos: " + str(descontos))

main()

