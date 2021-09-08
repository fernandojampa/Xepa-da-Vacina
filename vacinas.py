class Vacinas:
    def __init__(self):
        self._quantidade = 0

    @property
    def quantidade(self):
        return self._quantidade

    @quantidade.setter
    def quantidade(self, quantidade):
        self._quantidade = quantidade

    def vazio(self):
        return self._quantidade == 0  # returna True ou False

    def tamanho(self):
        return self._quantidade

    def atualizarDoses(self, estoque):
        self._quantidade = estoque
