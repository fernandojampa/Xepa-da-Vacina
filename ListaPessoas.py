import random
#from vacinas import Vacinas


class ListaException(Exception):
    def __init__(self, mensagem):
        super().__init__(mensagem)


class Agendamento:
    def __init__(self):
        self._agendamento = []
        self._doses = 0

    @property
    def doses(self):
        return self._doses

    @doses.setter
    def doses(self, valor):
        self._doses = valor

    @property
    def agendamento(self):
        return self._agendamento

    @agendamento.setter
    def agendamento(self, novo):
        self._agendamento = novo

    def atualizarDoses(self, estoque):
        self._doses = estoque

    def dosesQuantidade(self):
        return self._doses

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

    def sorteio(self, k):

        if self.vazio():
            raise ListaException('Não há ninguém na fila!')

        pointer = random.randint(1, self.tamanho())
        print(f'O Pointer sorteado foi: {self._agendamento[pointer-1]}')

        while True:

            for i in range(len(self._agendamento)):
                if i+1 == pointer:
                    print(f'Pointer -> {pointer} : {self._agendamento[i]}')
                    print(f'Removido {self._agendamento[i]}')
                    self._agendamento.pop(i)
                    print(f'{self._agendamento}')
                    break

    def __str__(self):
        return self._agendamento.__str__()

    def imprimir(self):
        print(self.__str__())
