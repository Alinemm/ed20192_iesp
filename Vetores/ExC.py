def main1():
    registro = [45,86]

    tamanho = int(input("Quantos elementos a inserir? "))

    for i in range(0,tamanho):
        tmp = input("Valor "+ str(i)+ ": ")
        registro.append(tmp)

    print(registro)

def main2():
    registro = input("Digite os valores, separados por vírgula: ").split(",")
    print(registro)


main1()
main2()
