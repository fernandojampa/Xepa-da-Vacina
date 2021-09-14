from vacinas import Vacinas
from ListaPessoas import Agendamento, ListaException

sistema_agendamento = Agendamento()
sistema_vacinas = Vacinas()

if __name__ == "__main__":
    # input do menu

    while True:
        try:

            print('''
Sistema de Vacinas para Agendamentos e Sorteios\n
      (1) Agendar vacina
      (2) Informar quantidade de doses remanescentes
      (3) Iniciar sorteio das doses
      (4) Visualizar agendamento
      (5) Consultar doses remanescentes
      (x) Sair do programa
            ''')

            opcao = input('Insira a opção desejada: ').lower()
            # Cadeia de ifs de acordo com as opções do menu

            if opcao == '1':
                sistema_agendamento.inserir('Maria')
                sistema_agendamento.inserir('Ândrei')
                sistema_agendamento.inserir('Fernando')
                sistema_agendamento.inserir('Jorge')
                sistema_agendamento.inserir('Candido')
                sistema_agendamento.inserir('Alex')
                sistema_agendamento.inserir('Edemberg')
                sistema_agendamento.inserir('Thiago')

                #nome = input('Informe seu nome: ')
                # if nome.replace(" ","").isalpha():
                # sistema_agendamento.inserir(nome)
                #print (f'\n{nome}, seu agendamento foi realizado com sucesso!')

                # else:
                #print("\nPor favor, insira um nome válido!")

            elif opcao == '2':
                try:
                    fabricante = input('Informe o fabricante: ')
                    if fabricante.replace(" ", "").isalpha():
                        sistema_vacinas.inserir_fabricante(fabricante)
                        print(f'\n{fabricante}, cadastrado com sucesso!')
                        valor = int(input(
                            f'\nInforme a quantidade de doses remanescentes do fabricante {fabricante}: '))
                        sistema_vacinas.inserir_doses(valor)
                        sistema_agendamento.gambiarra(valor)

                    else:
                        print("\nPor favor, insira um nome válido!")

                except ValueError:
                    print(
                        '\n!- Erro na Operação -!\n\nValor inserido não foi um valor válido. Por favor, tente novamente inserindo um número inteiro.')

            elif opcao == '3':
                try:
                    sistema_agendamento.sorteio()
                except ListaException as e:
                    print(e)

            elif opcao == '4':

                print(sistema_agendamento.visualizar_agendamento())

            elif opcao == '5':

                print(sistema_vacinas.quantidade_doses_total())
                sistema_vacinas.quantidade_doses_fabricante()

               # Opção para encerrar o programa.

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
