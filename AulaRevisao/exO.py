def main():
    inicio = int(input("número do início do intervalo: ")) 
    fim = int(input("número do fim do intervalo: "))

    for i in range(inicio,fim+1):
        print(i**2)

main()