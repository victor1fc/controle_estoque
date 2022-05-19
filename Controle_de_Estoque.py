# Código elaborado por Victor Fernandes Campos para a disciplina de Lógica de Programação e Algoritmos

def cadastrarPeca(codigo):
    print('Você selecionou a opção: Cadastrar peça...')
    print('Código da peça {}'. format(codigo))
    nome = input('Por favor, entre com o NOME da peça: ')
    fab = input('Por favor, entre com o FABRICANTE da peça: ')
    valor = float(input('Por favor, entre com o VALOR(R$) da peça: '))
    estoque = {'código': codigo,                             # Atribui os dados da peça em um dicionario
               'nome': nome.upper(),                         # grava o nome em maiúsculo para facilitar a identificação
               'fabricante': fab.upper(),              # grava o fabricante em maiúsculo para facilitar a identificação
               'valor': valor
               }
    listaEstoque.append(estoque.copy())                         # Insere esse dicionário numa lista
    print('Peça cadastrada!')

def consultarPeca():
    print('Você selecionou a opção: Consultar peça...')
    while True:
        try:                                          # Tratamento de erro caso valor de 'op' inserido não for númerico
            print('Escolha a opção desejada:')
            print('1 - Consultar Todas as Peça')
            print('2 - Consultar Peças por Código')
            print('3 - Consultar Peças por Fabricante')
            print('4 - Retornar')
            op = int(input('Opção: '))
            if (op < 1) or (op > 4):                # Repete caso insira valor diferente das opçoes disponiveis no menu
                print('Opção Inválida!')
                continue
        except:                                    # Repete caso valor de 'op' inserido não for númerico
            print('Opção Inválida!')
            continue

        else:                                              # Se opção selecionada for válida

            if op == 1:
                print('TODAS as peças cadastradas:')
                for k in listaEstoque:                      # Navega por cada dicionário dentro da lista
                    for i,j in k.items():                   # Navega por cada chave/valor dentro do dicionário
                        print('{}: {}'.format(i,j))         # Imprime cada chave e valor (dados da peça)

            elif op == 2:
                print('Consultar peças por código selecionado!')
                cod = int(input('Digite o CÓDIGO da peça: '))
                flag_encontrado = 0                             # Flag para verificar se o código está cadastrado
                for pecas in listaEstoque:                      # Navega por cada dicionário dentro da lista
                    if pecas['código'] == cod:       # Se encontrar o código inserido na chave 'código' do dicionário...
                        flag_encontrado = 1
                        for i, j in pecas.items():   #...imprime dados dessa peça
                            print('{}: {}'.format(i, j))

                if flag_encontrado == 0:                        # Flag não alterada. Portanto, código não cadastrado
                        print ('Código inexistente!')
                        continue                                # Volta para o menu
            elif op == 3:
                print('Consultar peças por fabricante selecionado!')
                fabric = input('Digite o FABRICANTE da peça: ')
                flag_encontrado = 0
                for pecas in listaEstoque:                          # Percorre os dicionários dentro da lista
                    if pecas['fabricante'] == fabric.upper():     # Se encontrar o fabricante inserido na chave 'código'
                                                                  # do dicionário
                        flag_encontrado = 1
                        for i, j in pecas.items():                  # imprime dados dessa(s) peça(s)
                            print('{}: {}'.format(i, j))
                if flag_encontrado == 0:                       # Flag não alterada. Portanto, fabricante não encontrado
                    print('Fabricante não encontrado!')
                    continue
            elif op == 4:                                           # Retorna para o main
                break


def removerPeca():
    print('Você selecionou a opção: Remover peça...')
    try:                                         # Tratamento de erro caso valor de 'remover' inserido não for númerico
        remover = int(input('Digite o código da peça a ser removida: '))
        flag_encontrado = 0
        for pecas in listaEstoque:                  # Procura pelo código da peça a ser removida
            if pecas['código'] == remover:
                flag_encontrado = 1                 # Flag indicando que o código foi encontrado
                listaEstoque.remove(pecas)          # Remove esse dicionário da lista de estoque
                print('Peça removida com sucesso!')

        if flag_encontrado == 0:                    # Flag não alterada. Portanto, código inexistente
            print('Código inexistente!')
            print('Remoção falhou!')
    except:                                         # Repete caso valor de 'remover' inserido não for númerico
       print('Você digitou valor não numérico!')
       print('Tente novamente...')



#----------------- MAIN inicio -------------------------
print ('Bem vindo ao Controle de Estoque da Bicicletaria do Victor Fernandes Campos')
contador = 3959710                                      # Código da peça baseada no meu RU
listaEstoque = []

while True:
    try:                                       # Tratamento de erro caso valor de 'op' inserido não for númerico
        print('Escolha a opção desejada:')
        print('1 - Cadastrar Peça')
        print('2 - Consultar Peça')
        print('3 - Remover Peça')
        print('4 - Sair')
        op = int(input('Opção: '))
        if (op < 1) or (op > 4):               # Repete caso insira valor diferente das opçoes disponiveis no menu
            print('Opção Inválida!')
            continue

    except:                                     # Repete caso valor de 'op' inserido não for númerico
        print('Opção Inválida!')
        continue

    else:                                       # Opção selecionada válida e chama função correspondente
        if op == 1:
            cadastrarPeca(contador)
            contador += 1                       # Novo código para a próxima peça
        elif op == 2:
            consultarPeca()
        elif op == 3:
            removerPeca()
        elif op == 4:
            break
#----------------- MAIN final -------------------------
