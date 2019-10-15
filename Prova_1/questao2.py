def main():
  vetor = []
  for i in range(20):
    vetor.append(int(input("Digite um número: ")))

  for i in range(len(vetor)):
    if (vetor[i] <=10):
      print("o termo " + str(vetor[i]) + " está na posição " + str(i))
main()
