# Estrutura de dados
voos = {}  # chave: número do voo, valor: dicionário com informações do voo
passageiros = {}  # chave: CPF do passageiro, valor: dicionário com nome e telefone
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

    # voos[numero] = {
    #     "origem": origem,
    #     "destino": destino,
    #     "escalas": escalas,
    #     "preco": preco,
    #     "lugares": lugares
    # }

    voos[numero] = [origem, destino, escalas, preco, lugares]


    # No ato de vender a passagem, a gente pega essa lista e adiciona os dados do passageiro na lista referenciada.
    voos_passageiros[numero] = []
    print("Voo cadastrado com sucesso.")

def consultar_voo():
    codigo = input('Digite o código do voo: ')

    while codigo not in voos:
        print('digite um codigo existente ou digite "quit" para sair')
        codigo = input('Digite o código do voo: ')

        if codigo.strip().lower() == 'quit':
            return
        
    
    voo = voos[codigo]
    
    print(f'Origem: {voo[0]}\nDestino: {voo[1]}\nNumero de escalas: {voo[2]}\nPreço da passagem: {voo[3]}\nQuantidade de lugares disponíveis: {voo[4]}')

def menu():

    opcoes = {
        '1': [cadastrar_voo, 'Cadastrar voo'],
        '2': [consultar_voo, 'Consultar voo']
    }
    for i in opcoes:
        print(f'{i} - {opcoes[i][1]}')

    escolha = input('Digite o numero do item que quer fazer: ')
    if escolha not in opcoes:
        print('Dá não')
        return
    
    opcoes[escolha][0]()

menu()
print(voos)
print(voos_passageiros)
print('-'*40)



