from datetime import datetime
from vacinas import Vacinas
import random


class ListaException(Exception):
    def __init__(self, mensagem):
        super().__init__(mensagem)


class Agendamento:
    def __init__(self):
        self._agendamento = []
        self._contemplados = []  # fazer encapsulamento
        self._gambiarra = 0
        self._k = 0  # fazer encapsulamento

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

    def vazio(self):
        if len(self._agendamento) == 0:
            return ("A lista de pessoas está vazia!")  # returna True ou False

    def tamanho(self):
        return len(self._agendamento)

    def visualizar_agendamento(self):
        if not self._agendamento:
            return ("\nNão existem pessoas agendadas.")
        else:
            return (f'\nLista de pessoas agendadas:\n{self._agendamento}')

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

    def gambiarra(self, valor):
        self._gambiarra += valor

    def sorteio(self):

        if self.vazio():
            raise ListaException("\nNão há ninguém agendado para o sorteio!")

        else:
            print('Iniciando sorteio...')
            #k = random.randint(1, self.tamanho())
            k = 2
            print(f'k escolhido: {k}')
            self._k = k
            pointer = random.randint(1, self.tamanho())
            print(f'O Pointer sorteado foi: {self._agendamento[pointer-1]}\n')

            while self._gambiarra != 0:
                self._gambiarra -= 1

                print(f'Lista: {self._agendamento}')
                print(f'Pointer -> {pointer} : {self._agendamento[pointer-1]}')
                ultimo = len(self._agendamento)
                contador = 0
                condicao = False
                while contador != k:
                    ultimo = len(self._agendamento)

                    if pointer == ultimo:
                        pointer = 1

                    else:
                        pointer += 1
                    contador += 1
                    if pointer == ultimo and contador == k:
                        condicao = True
                        aux = pointer
                        pointer = 1
                        print(f'removido: {self._agendamento[aux-1]}')
                        self._contemplados.append(self._agendamento[aux-1])
                        self._agendamento.pop(aux-1)
                        break

                if condicao == False:
                    print(f'removido: {self._agendamento[pointer-1]}\n')
                    self._contemplados.append(self._agendamento[pointer-1])
                    self._agendamento.pop(pointer-1)
                    print()

            self.imprimir()

    def imprimir(self):

        print(datetime.today().strftime('%d/%m/%Y'))
        #print(f'Doses disponíveis: {doses.quantidade_doses_total()}')
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
