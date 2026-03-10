import os
os.system("cls || clear")
# 1. Coleta de dados básicos
nome = input("Digite o nome: ")
sexo = input("Digite o sexo (M/F): ").upper()  # .upper() padroniza para maiúsculo
estado_civil = input("Digite o estado civil: ").upper()

tempo_casada = None

# 2. Verificação Condicional
# O bloco abaixo só será executado se AMBAS as condições forem verdadeiras
if sexo == "F" and estado_civil == "CASADA":
    tempo_casada = input("Há quantos anos você está casada? ")

# 3. Exibição dos dados
print("\n--- Dados do Usuário ---")
print(f"Nome: {nome}")
print(f"Sexo: {sexo}")
print(f"Estado Civil: {estado_civil}")

# Só mostra o tempo de casada se a variável tiver sido preenchida
if tempo_casada:
    print(f"Tempo de casada: {tempo_casada} anos")