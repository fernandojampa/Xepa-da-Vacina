from datetime import datetime
import random
#from vacinas import Vacinas


class ListaException(Exception):
    def __init__(self, mensagem):
        super().__init__(mensagem)


class Agendamento:
    def __init__(self):
        self._agendamento = []
        self._contemplados = []
        self._doses = 0
        self._doses2 = 0
        self._k = 0

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
        self._doses2 = self._doses

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
        self._k = k
        if self.vazio():
            raise ListaException('Não há ninguém na fila!')

        pointer = random.randint(1, self.tamanho())
        print(f'O Pointer sorteado foi: {self._agendamento[pointer-1]}')
        print()

        while self._doses != 0:
            self._doses -= 1

            print(f'Lista: {self._agendamento}')
            print(f'Pointer -> {pointer} : {self._agendamento[pointer-1]}')
            #print(f'Removido {self._agendamento[i]}')
            ultimo = len(self._agendamento)
            contador = 0
            while contador != k:
                ultimo = len(self._agendamento)
                if (pointer == ultimo):
                    pointer = 1
                else:
                    pointer += 1
                contador += 1
                if (pointer == ultimo and contador == k):
                    self._contemplados.append(
                        self._agendamento[pointer-1])
                    self._agendamento.pop(pointer-1)
                    pointer = 1
            print(f'removido: {self._agendamento[pointer-1]}')
            #print(f'pointer: {pointer}')
            self._contemplados.append(self._agendamento[pointer-1])
            self._agendamento.pop(pointer-1)
            print()

        self.imprimir()

    def imprimir(self):

        print(datetime.today().strftime('%d/%m/%Y'))
        print(f'Doses disponíveis: {self._doses2}')
        #Pfizer = 2
        #Coronavac = 3
        print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
        print(f'Selecionados (k = {self._k})')
        print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
        for i in range(len(self._contemplados)):
            print(self._contemplados[i])
        print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
        print('Não contemplados (fazer novo agendamento)')
        print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
        for i in range(len(self._agendamento)):
            print(self._agendamento[i])

    def __str__(self):
        pass
