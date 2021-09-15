from datetime import datetime

class Vacinas:
    def __init__(self):
        self._fabricante = []
        self._quantidade_doses = []

    # Encapsulamento dos atributos

    @property
    def quantidade_doses(self):
        return self._quantidade_doses

    @quantidade_doses.setter
    def quantidade_doses(self, quantidade):
        self._quantidade_doses = quantidade

    @property
    def fabricante(self):
        return self._fabricante
    
    @fabricante.setter
    def fabricante(self, fabricante):
        self._fabricante = fabricante

    # Método para inserir o nome do fabricante na lista.

    def inserir_fabricante(self, fabricante):
        self.fabricante.append(fabricante)
    
    # Método para inserir a quantidade de doses.

    def inserir_doses(self, quantidade):
      if quantidade > 0:
        self.quantidade_doses.append(quantidade)
      else:
        return ('\nQuantidade inválida! Por favor insira um número inteiro positivo.')
      
    # Método para imprirmir fabricante e a quantidade de suas doses, respectivamente.

    def quantidade_doses_fabricante(self):

        print('\nRelatório de ', end='')
        print(datetime.today().strftime('%d/%m/%Y'))
        for i in range(len(self.fabricante)):
          print(f'\nFabricante: {self.fabricante[i]}\nQuantidade: {self.quantidade_doses[i]}')