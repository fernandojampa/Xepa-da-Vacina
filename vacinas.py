class Vacinas:
    def __init__(self):
        self._fabricante = []
        self._quantidade_doses = []
        self._doses = 0

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

    def inserir_fabricante(self, fabricante):
        self.fabricante.append(fabricante)

    def inserir_doses(self, quantidade):
        self.quantidade_doses.append(quantidade)
        self._doses += quantidade

    def quantidade_doses_total(self):
        if not self.quantidade_doses:
            return('\nNão há doses disponíveis para o sorteio.')
        else:
            soma = 0
            for i in range(self.tamanho()):
                soma += self.quantidade_doses[i]
            return(f'\nHá {soma} doses disponíveis para o sorteio.')

    def quantidade_doses_fabricante(self):
        for i in range(len(self.fabricante)):
            print(
                f'\nFabricante: {self.fabricante[i]}\nQuantidade: {self.quantidade_doses[i]}')

    def vazio(self):
        return self._quantidade_doses == 0  # returna True ou False

    def tamanho(self):
        return len(self.quantidade_doses)

    def atualizarDoses(self, estoque):
        self._quantidade_doses = estoque
