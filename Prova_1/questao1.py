def verificaAno(anoL):
  msg = "Esse ano é bissexto!"
  
  if (anoL >= 1900 and anoL <= 100000):
    if(anoL % 4 == 0):
      if(anoL % 100 == 0):
        msg = "Esse ano não é bissexto!"
        if(anoL % 400 == 0):
          msg = "Esse ano é bissexto!"
    else:
      msg = "Esse ano não é bissexto!"     
  else:
    msg = "Esse ano não é aceito para o cálculo!"

  return msg

def main():
  op =  True

  while(op==True):
    ano = int(input("Digite o ano: "))
    print(verificaAno(ano))
    op = input("Deseja continuar (s/n)? ")
    if (op == "s" or op == "S"):
      op = True
    else:
      op = False

main()
