import pilhaArq

#ex5
def main():
  pilhaVar = Pilha()

  for i in range (5):
    pilhaVar.pushPilha(input("Estado: "))

  print('Topo: ',,pilhaVar.topo())

main()
