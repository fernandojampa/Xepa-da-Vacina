#from vacinas import Vacinas
from ListaPessoas import Agendamento, ListaException


lista_atual = Agendamento()
#doses = Vacinas()

if __name__ == "__main__":
    # input do menu

    while True:
        try:

            print('''
      (1) Agendar Vacina
      (2) Informar quantidade de doses remanescentes
      (3) Iniciar sorteio das doses
      (4) Visualizar agendamento
      (5) Consultar doses remanescentes
      (x) Sair do programa
            ''')

            opcao = input('Insira a opção desejada: ').lower()
            # Cadeia de ifs de acordo com as opções do menu

            # Opção de inserir valor no início da lista, com a chamada do respectivo método: inserir.inicio.

            if opcao == '1':
                try:
                    #nome = input('Informe seu nome: ')
                    # lista_atual.inserir(nome)

                    lista_atual.inserir('Fernando')
                    lista_atual.inserir('Maria')
                    lista_atual.inserir('Andrei')
                    lista_atual.inserir('Candido')
                    lista_atual.inserir('Alex')
                    lista_atual.inserir('Edemberg')
                    lista_atual.inserir('Jorge')
                    lista_atual.inserir('Leonidas')

                    #print ("Valor inserido no início da lista.")
                except ValueError:
                    print(
                        '\n!- Erro na Operação -!\n\nValor inserido não foi um valor válido. Por favor, tente novamente inserindo um número inteiro.')

            # Opção de inserir valor no final da lista, com a chamada do respectivo método: inserir.final

            elif opcao == '2':
                try:
                    valor = int(
                        input('Informe quantidade de doses remanescentes: '))
                    lista_atual.atualizarDoses(valor)

                except ValueError:
                    print(
                        '\n!- Erro na Operação -!\n\nValor inserido não foi um valor válido. Por favor, tente novamente inserindo um número inteiro.')

            # Opção de buscar um valor na lista, com a chamada do respectivo método: busca.

            elif opcao == '3':
                k = int(input('Informe o valor de k: '))
                print('Iniciando sorteio...')
                try:
                    print(lista_atual.sorteio(k))

                except ListaException as e:
                    print(e)
                except ValueError:
                    print(
                        '\n!- Erro na Operação -!\n\nValor inserido não foi um valor válido. Por favor, tente novamente inserindo um número inteiro.')

            elif opcao == '4':
                print('Lista das pessoas agendadas')
                try:
                    print(lista_atual.agendamento())

                except ListaException as e:
                    print(e)

                except ValueError:
                    print(
                        '\n!- Erro na Operação -!\n\nValor inserido não foi um valor válido. Por favor, tente novamente inserindo um número inteiro.')

            elif opcao == '5':
                print('Consultar doses remanescentes')
                try:
                    print(lista_atual.dosesQuantidade())

                except ListaException as e:
                    print(e)
                except ValueError:
                    print(
                        '\n!- Erro na Operação -!\n\nValor inserido não foi um valor válido. Por favor, tente novamente inserindo um número inteiro.')

             # Opção para encerrar o programa.

            elif opcao == 'x':
                break

            # Estrutura de decisão para caso o usuário digite algum valor não referente a nenhuma opção no menu, fazendo com que o laço reinicie.

            else:
                print(
                    '\nOpção inválida. Por favor, insira uma letra referente à uma das opções que estejam no menu. ')

             # Tratamento de erro caso o usuário pressione as teclas que encerram a aplicação.

        except KeyboardInterrupt:
            print('\n !- Erro na Operação -!')
            print('\nComando de teclas pare encerrar a aplicação pressionadas. Por favor, para sair do programa, insira a opção correspondente, no menu principal.')
'''
Menu
solicitar a lista de pessoas para se vacinar
solicitar o valor de k (número será aleatório)
solicitar a quantidade de doses
'''
