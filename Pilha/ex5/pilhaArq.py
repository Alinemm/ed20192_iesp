class Pilha(object):
    def __init__(self):
      #self.variavel = ["Amarelo", "Vermelho","Verde", "Azul"] #ex1,ex2,ex3
      self.variavel = [] #ex4 e ex5

    def getPilha(self):
      return self.variavel

    def pushPilha(self,dado):
      self.variavel.append(dado)  

    def popPilha(self):
      self.variavel.pop() 

    def topo(self):
      return self.variavel[len(self.variavel)-1]
