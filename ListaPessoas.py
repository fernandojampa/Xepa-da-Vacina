import random
from vacinas import Vacinas


class ListaException(Exception):
    def __init__(self, mensagem):
        super().__init__(mensagem)


class Agendamento:
    def __init__(self):
        self._agendamento = []

    @property
    def agendamento(self):
        return self._agendamento

    @agendamento.setter
    def agendamento(self, novo):
        self._agendamento = novo

    def vazio(self):
        return len(self._agendamento) == 0  # returna True ou False

    def tamanho(self):
        return len(self._agendamento)

    def topo(self):
        if self.vazio():
            raise ListaException('Doses esgotadas!')
        return self._agendamento[0]

    def inserir(self, nome):
        self._agendamento.append(nome)

    def remover(self):
        if self.vazio():
            raise ListaException('Doses esgotadas!')
        return self._agendamento.pop()

    def sorteio(self):

        if self.vazio():
            raise ListaException('Não há ninguém na fila!')

        k = random.randint(1, self.tamanho())
        return f'tamanho sorteado de k: {k}'

    def __str__(self):
        return self._agendamento.__str__()

    def imprimir(self):
        print(self.__str__())
