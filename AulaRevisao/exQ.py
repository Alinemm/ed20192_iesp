#Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual número ele deseja ver a tabuada.

def main():
   numero = int(input("Digite o número que você gostaria de saber a tabuada: "))

   for i in range(0,11):
       resultado = numero * i
       print(i, "x", numero, " = ", resultado)

main()