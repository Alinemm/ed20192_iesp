import pilhaArq

def main():
  pilhaVar = Pilha()
  pilhaVar.pushPilha('iesp')
  pilhaVar.pushPilha('ufpb')
  pilhaVar.pushPilha('ufcg')
  pilhaVar.pushPilha('ifpb')
  pilhaVar.pushPilha('mit')
  pilhaVar.pushPilha('harvard')

  print(pilhaVar.getPilha())

  while(len(pilhaVar.getPilha())!=0):
    pilhaVar.popPilha()

  print(pilhaVar.getPilha())

main()
