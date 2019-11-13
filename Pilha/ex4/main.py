import pilhaArq

def main():
  pilhaVar = Pilha()

  for i in range (3):
    pilhaVar.pushPilha(input("Qual é o seu nome ou sobrenome? "))

  print(pilhaVar.getPilha())
  pilhaVar.popPilha()
  print(pilhaVar.getPilha())

main()
