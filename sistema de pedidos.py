# Objetivo: criar um programa que agende pedidos de uma lancheria
# O cliente pode escolher:
# O produto
# Método de pagamento
# Após, receberá uma confirmação de pedido
# Irá perguntar: Produtos + "Deseja confirmar o pedido?"
# AGRADECIMENTOS
# ~=~=~=~=~=~=~=~=~=~=~=~==~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=
# Os produtos:

# - Bauru Gigante (R$20,00)
# Pão, frango, porco, bacon, calabresa, coração, queijo duplo, presunto, 2 ovos
# Milho, ervilha, batata palha, maionese, alface e tomate
# - Filé (R$28,00)
# Pão, filé, ovo, queijo, maionese, alface e tomate
# - Entrecot (R$22,00)
# Pão, entrecot, ovo, queijo, maionese, alface e tomate
# - Calabresa com bacon (R$22,00)
# Pão, calabresa, bacon, ovo, queijo, milho, ervilha, maionese, alface e tomate
# - Bacon (R$19,00)
# Pão, bacon, queijo, presunto, milho, ervilha, ovo, maionese, alface e tomate
# - Coração (R$19,00)
# Pão, coração, ovo, queijo, maionese, alface, tomate
# - Calabresa (R$15,00)
# Pão, calabresa, ovo, queijo, maionese, alface e tomate
# - Xis Frango (R$15,00)
# Pão, frango, ovo, queijo, maionese, alface e tomate
# =~=~=~=~=~=~=~=~=~=~=~=~~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~~=~=~=~=~=
# Métodos de pagamento:
# - PIX
# - Crédito
# - Débito
# - Dinheiro (Com ou sem troco?)

bauru = 20
file = 28
entrecot = 22
calabresabacon = 22
bacon = 19
coracao = 19
calabresa = 15
frango = 15
coca = 10
fanta = 9
suco = 6

def lanches():
    print('''1 - BAURU GIGANTE (R$20,00)\n(Pão, frango, porco, bacon, calabresa, coração, queijo duplo, presunto, 2 ovos, milho, ervilha, batata palha, maionese, alface, tomate)
2 - FILÉ (R$28,00)\n(Pão, filé, ovo, queijo, maionese, alface, tomate)
3 - ENTRECOT (R$22,00)\n(Pão, entrecot, ovo, queijo, maionese, alface e tomate)
4 - CALABRESA COM BACON (R$22,00)\n(Pão, calabresa, bacon, ovo, queijo, milho, ervilha, maionese, alface e tomate)
5 - BACON (R$19,00)\n(Pão, bacon, queijo, presunto, milho, ervilha, ovo, maionese, alface e tomate)
6 - CORAÇÃO (R$19,00)\n(Pão, coração, ovo, queijo, maionese, alface, tomate)
7 - CALABRESA (R$15,00)\n(Pão, calabresa, ovo, queijo, maionese, alface e tomate)
8 - XIS FRANGO (R$15,00)\n(Pão, frango, ovo, queijo, maionese, alface e tomate)
''')
    global lanche
    lanche = int(input('Selecione o número do lanche que deseja: '))
    if lanche == 1:
        lanche = bauru
        print('Que delícia! Você optou por um BAURU GIGANTE.')
    elif lanche == 2:
        lanche = file
        print('Que delícia! Você optou por um FILÉ.')
    elif lanche == 3:
        lanche = entrecot
        print('Que delícia! Você optou por um ENTRECOT.')
    elif lanche == 4:
        lanche = calabresabacon
        print('Que delícia! Você optou por um CALABRESA COM BACON.')
    elif lanche == 5:
        lanche = bacon
        print('Que delícia! Você optou por um XIS BACON.')
    elif lanche == 6:
        lanche = coracao
        print('Que delícia! Você optou por um XIS CORAÇÃO.')
    elif lanche == 7:
        lanche = calabresa
        print('Que delícia! Você optou por um XIS CALABRESA.')
    elif lanche == 8:
        lanche = frango
        print('Que delícia! Você optou por um XIS FRANGO.')
    else:
        print('\033[31m\nOPÇÃO INVÁLIDA! TENTE NOVAMENTE.\033[m\n')
        lanches()


def add_bebida():
    print('Deseja adicionar bebida?\n1 - SIM\n2 - NÃO')
    global drink
    drink = int(input('Sua opção: '))
    if drink == 1:
        bebidas()
    elif drink == 2:
        print('OK! vamos ao pagamento.')
        print('VALOR TOTAL DO SEU PEDIDO: R${:.2f}'.format(lanche))
        formas_pagamento()
    else:
        print('\033[31m\nOPÇÃO INVÁLIDA! TENTE NOVAMENTE!\033[m\n')
        lanches()


def bebidas():
    print('1 - Coca-cola (R$10,00)\n2 - Fanta (R$9,00)\n3 - Suco de Laranja (R$6,00)\n4 - Voltar')
    global bebida
    bebida = int(input('Sua opção: '))
    if bebida == 1:
        print('Deseja adicionar uma Coca-Cola ao seu pedido?\n1 - SIM\n2 - NÃO')
        confirmacao = int(input('Sua opção: '))
        if confirmacao == 1:
            bebida = coca
            print('Coca-Cola adicionada no pedido!')
            print('Adicionar mais bebidas?\n1 - SIM\n2 - NÃO')
            adicionar = int(input('Sua opção: '))
            if adicionar == 1:
                bebidas()
            elif adicionar == 2:
                print('OK! Vamos ao pagamento.')
                total()
                formas_pagamento()
            else:
                print('\033[31m\nOPÇÃO INVÁLIDA! TENTE NOVAMENTE!\033[m\n')
                bebidas()
        elif confirmacao == 2:
            bebidas()
        else:
            print('\033[31m\nOPÇÃO INVÁLIDA! TENTE NOVAMENTE!\033[m\n')
            bebidas()
    elif bebida == 2:
        print('Deseja adicionar uma Fanta ao seu pedido?\n1 - SIM\n2 - NÃO')
        confirmacao = int(input('Sua opção: '))
        if confirmacao == 1:
            bebida = fanta
            print('Fanta adicionada ao seu pedido!')
            print('Adicionar mais bebidas?\n1 - SIM\n2 - NÃO')
            adicionar = int(input('Sua opção: '))
            if adicionar == 1:
                bebidas()
            elif adicionar == 2:
                print('OK! Vamos ao pagamento.')
                total()
                formas_pagamento()
            else:
                print('\033[31m\nOPÇÃO INVÁLIDA! TENTE NOVAMENTE!\033[m\n')
                bebidas()
        elif confirmacao == 2:
            bebidas()
        else:
            print('\033[31m\nOPÇÃO INVÁLIDA! TENTE NOVAMENTE!\033[m\n')
    elif bebida == 3:
        print('Deseja adicionar um Suco de Laranja ao seu pedido?\n1 - SIM\n2 - NÃO')
        confirmacao = int(input('Sua opção: '))
        if confirmacao == 1:
            bebida = suco
            print('Um Suco de Laranja foi adicionado ao seu pedido!')
            print('Adicionar mais bebidas?\n1 - SIM\n2 - NÃO')
            adicionar = int(input('Sua opção: '))
            if adicionar == 1:
                bebidas()
            elif adicionar == 2:
                print('OK! Vamos ao pagamento.')
                total()
                formas_pagamento()
            else:
                print('\033[31m\nOPÇÃO INVÁLIDA! TENTE NOVAMENTE!\033[m\n')
                bebidas()
    elif bebida == 4:
        add_bebida()
    else:
        print('\033[31m\nOPÇÃO INVÁLIDA! TENTE NOVAMENTE!\033[m\n')
        bebidas()


def total():
    global soma
    soma = lanche + bebida
    print('VALOR TOTAL DO PEDIDO: R${:.2f}'.format(soma))


def formas_pagamento():
    print('SELECIONE A FORMA DE PAGAMENTO:\n1 - PIX\n2 - Crédito\n3 - Débito\n4 - Dinheiro')
    opcao = int(input('Sua opção: '))
    if opcao == 1:
        print('Chave pix: (99)999999999\nNos envie o comprovante no VALOR TOTAL DO PEDIDO e jajá iremos confirmar o seu pagamento.')
        agradecimentos()
        exit()
    elif opcao == 2:
        print('OK, nosso entregador levará a maquininha até você!')
        agradecimentos()
        exit()
    elif opcao == 3:
        print('OK, o entregador levará a maquininha até você!')
        agradecimentos()
        exit()
    elif opcao == 4:
        print('Você precisa de troco?\n1 - SIM\n2 - NÃO')
        troco = int(input('Sua opção: '))
        if troco == 1:
            quanto = float(input('Troco para quanto? R$'))
            print('OK! O entregador terá R${:.2f} de troco para R${:.2f}!'.format(
                (quanto - lanche), quanto))
            agradecimentos()
            exit()
        elif troco == 2:
            print('OK! Finalizamos o seu pedido!')
            agradecimentos()
            exit()
        else:
            print('\033[31m\nOPÇÃO INVÁLIDA! TENTE NOVAMENTE!\033[m\n')
            formas_pagamento()
    else:
        print('\033[31m\nOPÇÃO INVÁLIDA! TENTE NOVAMENTE!\033[m\n')
        exit()


def agradecimentos():
    print('\033[32mLANCHERIA BRASIL AGRADECE A SUA PREFERÊNCIA!\033[m')


print('~='*10, 'LANCHERIA BRASIL', '~='*10)
print('\n')
print('~='*3, 'CARDÁPIO', '~='*3, '\n')
print('§='*2, 'LANCHES', '§='*2, '\n')
lanches()
add_bebida()
