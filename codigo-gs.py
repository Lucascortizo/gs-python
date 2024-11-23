# Função principal
def principal():
    print("Seja bem-vindo à EnergyLink!")
    registros = []  # Lista para armazenar os consumos

    # Loop do menu
    while True:
        print("\nMenu:")
        print("1. Registrar consumo")
        print("2. Ver consumo total")
        print("3. Escolher planos")
        print("4. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            registrar_consumo(registros)
        elif escolha == "2":
            exibir_registros(registros)
        elif escolha == "3":
            exibir_planos()
        elif escolha == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

# Função para registrar consumo
def registrar_consumo(registros):
    data = input("Digite a data: ")
    consumo = input("Digite o consumo em KWh: ")

    # Verificar se o consumo é um número inteiro e adicionar para a lista registros
    if consumo.isnumeric():
        registros.append({"data": data, "consumo": consumo})
        print("Registro salvo!")
    else:
        print("Erro: Consumo deve ser um número válido.")

# Função para exibir registros de consumo
def exibir_registros(registros):
    if registros:
        print("\nRelatório de Consumo:")
        for registro in registros:
            print(f"Data: {registro['data']} | Consumo: {registro['consumo']} kWh")
    else:
        print("Nenhum registro encontrado.")

# Função para exibir planos de energia e escolher fornecedor
def exibir_planos():
    fornecedores = {
        "Energia Solar": ["Enel Green Power", "Atlas Renewable Energy", "Omega Energia", "Canadian Solar"],
        "Energia Eólica": ["EDP Renováveis", "Iberdrola", "Voltalia"],
        "Energia Hidrelétrica": ["Eletrobras", "CESP", "Copel"],
        "Biomassa": ["Raízen"],
        "Energia de Hidrogênio Verde": ["Green Hydrogen Alliance", "Hydroverde Brasil"],
        "Energia Geométrica": ["GeoEnergy Solutions"],
        "Energia Marítima": ["WavePower Inc."],
        "Petróleo": ["Petrobras", "Chevron", "Shell"],
        "Carvão Mineral": ["Vale", "Anglo American"],
        "Gás Natural": ["Naturgy", "Comgás"],
        "Energia Nuclear": ["Eletronuclear"]
    }
    
    print("\nPlanos de energia disponíveis:")
    print("\nEnergias Renováveis: (Recomendado)")
    print("1. Energia Solar")
    print("2. Energia Eólica")
    print("3. Energia Hidrelétrica")
    print("4. Biomassa")
    print("5. Energia de Hidrogênio Verde")
    print("6. Energia Geométrica")
    print("7. Energia Marítima")
    print("\nEnergias não sustentáveis:")
    print("8. Petróleo")
    print("9. Carvão Mineral")
    print("10. Gás Natural")
    print("11. Energia Nuclear")
    
    escolha = input("\nEscolha uma opção de 1 a 11 para ver os fornecedores: ")
    
    # Verifica se a opção escolhida é válida
    if escolha == "1":
        energia_escolhida = "Energia Solar"
    elif escolha == "2":
        energia_escolhida = "Energia Eólica"
    elif escolha == "3":
        energia_escolhida = "Energia Hidrelétrica"
    elif escolha == "4":
        energia_escolhida = "Biomassa"
    elif escolha == "5":
        energia_escolhida = "Energia de Hidrogênio Verde"
    elif escolha == "6":
        energia_escolhida = "Energia Geométrica"
    elif escolha == "7":
        energia_escolhida = "Energia Marítima"
    elif escolha == "8":
        energia_escolhida = "Petróleo"
    elif escolha == "9":
        energia_escolhida = "Carvão Mineral"
    elif escolha == "10":
        energia_escolhida = "Gás Natural"
    elif escolha == "11":
        energia_escolhida = "Energia Nuclear"
    else:
        print("Opção inválida. Tente novamente.")
        return
    
    # Exibe os fornecedores da energia escolhida
    print(f"\nVocê escolheu {energia_escolhida}, veja os fornecedores:")
    for fornecedor in fornecedores[energia_escolhida]:
        print(fornecedor)
    
    # Permite ao usuário escolher um fornecedor
    while True:
        fornecedor_escolhido = input("\nDigite o nome do fornecedor que você escolheu: ")
        if fornecedor_escolhido in fornecedores[energia_escolhida]:
            print(f"\nVocê escolheu o fornecedor {fornecedor_escolhido} para {energia_escolhida}.")
            break
        else:
            print("\nFornecedor inválido. Tente novamente.")

# Chamar a função principal para rodar o programa
principal()
