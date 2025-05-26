# Estrutura de dados 
voos = {}  # chave: número do voo, valor: lista com informações do voo
passageiros = {}  # chave: CPF do passageiro, valor: lista com nome e telefone
voos_passageiros = {}  # chave: número do voo, valor: lista de CPFs

# Função para cadastrar um novo voo
def cadastrar_voo():
    
    numero = input("Digite o número do voo: ")
    if numero in voos:
        print("Voo já cadastrado.")
        return
    
    origem = input("Digite a cidade de origem: ")
    destino = input("Digite a cidade de destino: ")
    escalas = int(input("Digite o número de escalas: "))
    preco = float(input("Digite o preço da passagem: "))
    lugares = int(input("Digite a quantidade de lugares disponíveis: "))

    voos[numero] = [origem, destino, escalas, preco, lugares]


    # No ato de vender a passagem, a gente pega essa lista e adiciona os dados do passageiro na lista referenciada.
    voos_passageiros[numero] = []
    print("Voo cadastrado com sucesso.")

def consultar_voo():
    codigo = input('Digite o código do voo: ')

    while codigo not in voos:
        print('digite um codigo existente ou digite "quit" para cancelar a operação')
        codigo = input('Digite o código do voo: ')

        if codigo.strip().lower() == 'quit':
            return
        
    
    voo = voos[codigo]
    
    print(f'Origem: {voo[0]}\nDestino: {voo[1]}\nNumero de escalas: {voo[2]}\nPreço da passagem: {voo[3]}\nQuantidade de lugares disponíveis: {voo[4]}')

def listar_voos():
    if len(voos) > 0:
        return
    for i in voos:
        cidade_embarque = voos[i][0]
        destino = voos[i][1]
        escalas = voos[i][2]
        preco = voos[i][3]
        lugares_disponiveis = voos[i][4]
        print('-'*30)
        print(f'VOO #{i}\nCidade de embarque: {cidade_embarque}\nDestino: {destino}\nEscalas: {escalas}\nPreço: R${preco}\nLugares disponíveis: {lugares_disponiveis}')
        print('-'*30)

def cadastrar_passageiro(cpf):
    nome = input('Digite seu nome: ')
    telefone = input('Digite seu telefone: ')
    passageiros[cpf] = [nome, telefone]
    

def venda_passagem():
    listar_voos()
    voo_selecionado = input('Digite o ID do voo que deseja: ')

    if voo_selecionado not in voos:
        print('Digite um ID valido')
        return
    
    voo = voos_passageiros[voo_selecionado]
    cpf = input('Digite seu CPF: ')

    if cpf in passageiros:
        if cpf not in voo:
            print('já existe em passageiros, usando informações existentes...')
            voo.append([passageiros[cpf][0], passageiros[cpf][1]])
            voos[voo_selecionado][4] -= 1 # Quantidade de lugares
            print('Usuário cadastrado com sucesso')
            return
        
        print('Usuario já cadastrado no voo.')
        return
    
    cadastrar_passageiro(cpf)
    voo.append([passageiros[cpf][0], passageiros[cpf][1]])
    voos[voo_selecionado][4] -= 1 

    
def mostrar_opcoes():
    opcoes = {
        '1': [cadastrar_voo, 'Cadastrar voo'],
        '2': [consultar_voo, 'Consultar voo'],
        '3': [venda_passagem, 'Vender passagem'],
        '4': ['cancelar_passagem', 'Cancelar passagem'],
        '5': [listar_voos, 'Listar voos'],
        '6': ['informar_voo_menor_escala', 'Informar o voo com menor escala'],
        '7': ['listar_passageiros_voo', 'Listar passageiros de um voo'],
        '8': [None, 'Sair']
    }
    for i in opcoes:
        print(f'{i} - {opcoes[i][1]}')
    
    return opcoes
    

def menu():
    opcoes = mostrar_opcoes()
    escolha = input('Digite o numero da operação que deseja realizar: ')
    
    while escolha != '8':
        
        if escolha not in opcoes:
            print('Escolha inválida')
        else:
            opcoes[escolha][0]()

        opcoes = mostrar_opcoes()
        escolha = input('Digite o numero da operação que deseja realizar: ')


menu()
print(voos_passageiros, 'DEBUGGGGGGGGGGG')
print('-'*40)
