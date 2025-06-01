voos = {}
passageiros = {}
voos_passageiros = {}


def cadastrar_voo():
    numero = input('Digite o número do voo: ')
    if numero in voos:
        print('Voo já cadastrado.')
        return

    origem = input('Digite a cidade de origem: ')
    destino = input('Digite a cidade de destino: ')

    escalas = int(input('Digite o número de escalas: '))
    erro = False
    if escalas < 0:
        print('Escala deve ser maior ou igual a zero.')
        erro = True

    preco = float(input('Digite o preço da passagem: '))

    if preco < 0:
        erro = True
        print('Preço deve ser maior ou igual a zero.')

    lugares = int(input('Digite a quantidade de lugares disponíveis: '))

    if lugares < 0:
        erro = True
        print('A quantidade de lugares deve ser maior ou igual a zero.')

    if not erro:
        voos[numero] = [origem, destino, escalas, preco, lugares]
        voos_passageiros[numero] = []
        print('Voo cadastrado com sucesso.')
        return

    print('Falha no cadastro do voo.')


def consultar_voo():
    print('1 - Consultar por código do voo')
    print('2 - Consultar por cidade de origem')
    print('3 - Consultar por cidade de destino')

    opcao = input('Escolha uma opção: ')

    if opcao == '1':
        codigo = input('Digite o código do voo: ')
        if codigo in voos:
            v = voos[codigo]
            print(
                f'Voo #{codigo}\nOrigem: {v[0]}\nDestino: {v[1]}\nEscalas: {v[2]}\nPreço: R${v[3]}\nLugares: {v[4]}')

        else:
            print('Voo não encontrado.')

    elif opcao == '2':
        origem = input('Digite a cidade de origem: ')
        for codigo, v in voos.items():
            if v[0].lower() == origem.lower():
                print(f'Voo #{codigo} -> Destino: {v[1]} | Preço: R${v[3]}')

    elif opcao == '3':
        destino = input('Digite a cidade de destino: ')
        for codigo, v in voos.items():
            if v[1].lower() == destino.lower():
                print(f'Voo #{codigo} -> Origem: {v[0]} | Preço: R${v[3]}')

    else:
        print('Opção inválida.')


def listar_voos():
    if len(voos) == 0:
        print('Não há voos cadastrados.')
        return

    for codigo, v in voos.items():
        print('-'*30)
        print(
            f'Voo #{codigo}\nOrigem: {v[0]}\nDestino: {v[1]}\nEscalas: {v[2]}\nPreço: R${v[3]}\nLugares disponíveis: {v[4]}')
        print('-'*30)


def cadastrar_passageiro(cpf, numero):
    nome = input('Digite o nome: ')
    telefone = input('Digite o telefone: ')
    if cpf in passageiros and passageiros[cpf][0] != nome:
        print('CPF já cadastrado com nome diferente.')
        return False

    passageiros[cpf] = [nome, telefone]
    voos_passageiros[numero].append(cpf)
    voos[numero][4] -= 1
    print('Passagem vendida com sucesso.')
    return True


def venda_passagem():
    listar_voos()
    voo = input('Digite o código do voo: ')
    if voo not in voos:
        print('Voo não encontrado.')
        return

    if voos[voo][4] <= 0:
        print('Voo lotado.')
        return

    cpf = input('Digite o CPF: ')
    if cpf in voos_passageiros[voo]:
        print('Passageiro já está nesse voo.')
        return

    if cpf in passageiros:
        print('Passageiro já cadastrado. Usando informações existentes.')
        voos_passageiros[voo].append(cpf)
        voos[voo][4] -= 1
        print('Passagem vendida com sucesso.')

    else:
        cadastrar = cadastrar_passageiro(cpf, voo)
        if not cadastrar:
            print('Falha na venda...')


def listar_passageiros_voo():
    listar_voos()
    codigo = input('Digite o código do voo: ')
    if codigo not in voos:
        print('Voo inválido.')
        return

    print('-'*40)

    for cpf in voos_passageiros[codigo]:
        dados = passageiros[cpf]
        print(f'Nome: {dados[0]}\nTelefone: {dados[1]}\nCPF: {cpf}\n')

    print(f'Lugares disponíveis: {voos[codigo][4]}')
    print('-'*40)


def cancelar_passagem():
    cpf = input('Digite o CPF do passageiro: ')
    if cpf not in passageiros:
        print('Passageiro não encontrado.')
        return

    encontrou = False
    for codigo, lista in voos_passageiros.items():
        if cpf in lista:
            v = voos[codigo]
            print('-'*30)
            print(f'Voo #{codigo}\nOrigem: {v[0]}\nDestino: {v[1]}')
            encontrou = True
            print('-'*30)

    if not encontrou:
        print('Este passageiro não possui voos.')
        return

    escolha = input('Digite o código do voo que deseja cancelar: ')
    if escolha in voos and cpf in voos_passageiros[escolha]:
        voos_passageiros[escolha].remove(cpf)
        voos[escolha][4] += 1
        print('Passagem cancelada com sucesso.')
    else:
        print('Informações inválidas.')


def voo_menor_escala():
    origem = input('Digite a cidade de origem: ')
    destino = input('Digite a cidade de destino: ')
    menor = None
    codigo = None
    for c, v in voos.items():
        if v[0].lower() == origem.lower() and v[1].lower() == destino.lower():
            if menor is None or v[2] < menor:
                menor = v[2]
                codigo = c
    if codigo:
        print(f'Voo com menor escala: #{codigo} com {menor} escalas.')

    else:
        print('Nenhum voo encontrado com essas cidades.')


def mostrar_opcoes():
    opcoes = {
        '1': [cadastrar_voo, 'Cadastrar voo'],
        '2': [consultar_voo, 'Consultar voo'],
        '3': [venda_passagem, 'Vender passagem'],
        '4': [cancelar_passagem, 'Cancelar passagem'],
        '5': [listar_voos, 'Listar voos'],
        '6': [voo_menor_escala, 'Informar o voo com menor escala'],
        '7': [listar_passageiros_voo, 'Listar passageiros de um voo'],
        '8': [None, 'Sair']
    }
    for i in opcoes:
        print(f'{i} - {opcoes[i][1]}')

    return opcoes


def main():
    opcoes = mostrar_opcoes()
    escolha = input('Digite o numero da operação que deseja realizar: ')

    while escolha != '8':

        if escolha not in opcoes:
            print('Escolha inválida')
        else:
            opcoes[escolha][0]()

        opcoes = mostrar_opcoes()
        escolha = input('Digite o numero da operação que deseja realizar: ')


main()
