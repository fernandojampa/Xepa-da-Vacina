from SistemaVacinas import Agendamento
from SistemaVacinas import ListaException

sistema_vacinas = Agendamento()

while True:
    try:

        print('''
Sistema de Vacinas para Agendamentos e Sorteios

      (1) Agendar vacina
      (2) Cadastrar doses remanescentes
      (3) Iniciar sorteio das doses
      (4) Consultar agendamento
      (x) Sair do programa
            ''')

        opcao = input('Insira a opção desejada: ').lower()

        # Cadeia de ifs de acordo com as opções do menu

        # Opção para inserir o nome dos candidatos.

        if opcao == '1':
            sistema_vacinas.inserir('Maria')
            sistema_vacinas.inserir('Fernando')
            sistema_vacinas.inserir('Cândido')
            sistema_vacinas.inserir('Alex')
            sistema_vacinas.inserir('Leonidas')
            sistema_vacinas.inserir('Jorge')
            sistema_vacinas.inserir('Ândrei')
            sistema_vacinas.inserir('Thiago')
            '''try:
                nome = input('Informe seu nome: ')        
                    
                if nome.replace(" ","").isalpha():
                  sistema_vacinas.inserir(nome)
                  print (f'\n{nome}, seu agendamento foi realizado com sucesso!')

                else:
                  print("\nPor favor, insira um nome válido!")

              except ListaException as e:
                print(e)'''

        # Opção para inserir os fabricantes e suas doses.

        elif opcao == '2':
            try:
                fabricante = input('Informe o fabricante: ')
                if fabricante.replace(" ", "").isalpha():

                    valor = int(input(
                        f'\nInforme a quantidade de doses remanescentes do fabricante {fabricante}: '))

                    sistema_vacinas.inserir_doses(valor)
                    sistema_vacinas.qtd_Doses(valor)
                    sistema_vacinas.inserir_fabricante(fabricante)
                    print(
                        f'\nFabricante {fabricante} e quantidade de doses cadastrados com sucesso!')

                else:
                    print("\nPor favor, insira um nome válido!")

            except ValueError:
                print(
                    '\nValor inserido não foi um valor válido. Por favor, tente novamente inserindo um número inteiro.')

            except ListaException as e:
                print(e)

        # Opção para realizar o sorteio.

        elif opcao == '3':
            try:
                k = int(input('Informe o valor de k: '))
                sistema_vacinas.sorteio(k)
                sistema_vacinas.quantidade_doses_fabricante()
                sistema_vacinas.imprimir()
                break
            except ListaException as e:
                print(e)

        # Opção para encerrar o programa.

        elif opcao == '4':
            print(sistema_vacinas.visualizar_agendamento())

        elif opcao == 'x':
            print('Programa encerrado!')
            break

        # Estrutura de decisão para caso o usuário digite algum valor não referente a nenhuma opção no menu, fazendo com que o laço reinicie.

        else:
            print(
                '\nOpção inválida. Por favor, insira um valor referente à uma das opções que estejam no menu. ')

        # Tratamento de erro caso o usuário pressione as teclas que encerram a aplicação.

    except KeyboardInterrupt:
        print('\n !- Erro na Operação -!')
        print('\nComando de teclas pare encerrar a aplia escolhapressionadas. Por favor, para sair do programa, insira a opção correspondente, no menu principal.')
