# Função principal
def principal():
    print("Seja bem-vindo à EnergyLink!")
    registros = []  # Lista para armazenar os consumos
#Cadastro
print("Faça seu Cadastro na EnergyLink")
user = input("Digite seu usuário")
while len(user) < 4:
    print ("Seu nome de usuário deve ter mais de 4 caracteres")
    user = input("Digite seu usuário")
while len(user) > 20:
    print ("Seu nome de usuário deve ter menos de 20 caracteres")
    user = input("Digite seu usuário")
nascimento = input("Digite sua data de Nascimento (DD/MM/AA)")
while not nascimento.isnumeric:
    print("Data Inválida")
    nascimento = input("Digite sua data de Nascimento (DD/MM/AAAA)")
senha = input("Digite sua senha")
confirma_senha = input("Confirme sua senha")
while not senha==confirma_senha:
    print ("As senhas não são iguais!")
    confirma_senha = input("Confirme sua senha")

    # Loop do menu
    while True:
        print("\nMenu:")
        print("1. Registrar consumo")
        print("2. Ver consumo total")
        print("3. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            registrar_consumo(registros)
        elif escolha == "2":
            exibir_registros(registros)
        elif escolha == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")


# Função para registrar consumo
def registrar_consumo(registros):
    data = input("Digite a data: ")
    consumo = input("Digite o consumo em KWh: ")

    # Verificar se o consumo é um número inteiro
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


# Chamar a função principal para rodar o programa
principal()
