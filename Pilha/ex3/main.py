import pilhaArq

def main():
  letras = Pilha()

  for i in range(5):
    caracter = input("Digite um caracter: ")
    letras.pushPilha(caracter)

  print(letras.getPilha())

main()
