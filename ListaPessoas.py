import random
from listaexception import ListaException

class Agendamento:
    def __init__(self):
        self._agendamento = []
        self._contemplados = []
        self._qtd_doses = 0

  # Encapsulamento dos atributos

    @property
    def agendamento(self):
        return self._agendamento

    @agendamento.setter
    def agendamento(self, novo):
        self._agendamento = novo

    @property
    def contemplados(self):
        return self._contemplados

    @contemplados.setter
    def contenplado(self, novo):
        self._contemplados = novo

    def atualizarDoses(self, estoque):
        self._doses = estoque

  # Método para chegar se o número de pessoas agendadas está Vazio.

    def vazio(self):
        if len(self._agendamento) == 0:
            return ("A lista de pessoas está vazia!")  # returna True ou False

  # Método para retornar o número total de pessoas agendadas.

    def tamanho(self):
        return len(self._agendamento)

  # Método para apresentar na tela as pessas agendadas.

    def visualizar_agendamento(self):
        if not self._agendamento:
            return ("\nNão existem pessoas agendadas.")
        else:
            return (f'\nLista de pessoas agendadas:\n\n{self._agendamento}')

  # Método para inserir uma pessoa na lista de agendamento.

    def inserir(self, nome):
      if nome in self._agendamento:
        raise ListaException ('\nNome já cadastrado!')
      else:
        return self._agendamento.append(nome)

  # Método para inserir doses totais para o sorteio. 

    def qtd_Doses(self, valor):
      if valor > 0:
        self._qtd_doses += valor
      else:
        raise ListaException ("\nQuantidade inválida! Por favor insira um número inteiro positivo.")

  # Método para realizar o sorteio das vacinas e apresentar na tela o seu processo.

    def sorteio(self):

        if self.vazio():
            raise ListaException("\nNão há ninguém agendado para o sorteio!")

        elif self._qtd_doses == 0:
            raise ListaException('\nNão há doses disponíveis para o sorteio!')

        else:
            print('\nIniciando sorteio...')
            k = random.randint(1, self.tamanho())
            print(f'k escolhido: {k}')
            pointer = random.randint(1, self.tamanho())
            print(f'O pointer sorteado foi: {self._agendamento[pointer-1]}\n')

            while self._qtd_doses != 0 and self.tamanho() > 0:
                self._qtd_doses -= 1

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
                        print(f'Contemplado: {self._agendamento[aux-1]}')
                        self._contemplados.append(self._agendamento[aux-1])
                        self._agendamento.pop(aux-1)
                        print()
                        break

                if condicao == False:
                    print(f'Contemplado: {self._agendamento[pointer-1]}\n')
                    self._contemplados.append(self._agendamento[pointer-1])
                    self._agendamento.pop(pointer-1)
                    print()

    # Método para imprimir o valor de k, pessoas contempladas ou não para a vacinação.

    def imprimir(self):
        print('\n+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
        print(f'\033[32m'+'Contemplados'+'\033[0;0m')
        print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
        for i in range(len(self._contemplados)):
            print(self._contemplados[i])
        print('\n+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
        print('\033[31m'+'Não Contemplados'+'\033[0;0m')
        print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
        for i in range(len(self._agendamento)):
            print(self._agendamento[i])