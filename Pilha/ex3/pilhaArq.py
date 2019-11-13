class Pilha(object):
    def __init__(self):
      self.variavel = ["Amarelo", "Vermelho","Verde", "Azul"]

    def getPilha(self):
      return self.variavel

    def pushPilha(self,dado):
      self.variavel.append(dado)

