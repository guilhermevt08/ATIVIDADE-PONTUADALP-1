import os
os.system

# 1. Entrada de dados
print("--- TABELA DE CORES DA LOJA ---")
print("Verde, Azul, Amarelo, Vermelho")
cor = input("Digite a cor do selo do CD: ").strip().lower()

# 2. Verificação da cor e definição do preço
if cor == "verde":
    preco = 10.00
elif cor == "azul":
    preco = 20.00
elif cor == "amarelo":
    preco = 30.00
elif cor == "vermelho":
    preco = 40.00
else:
    preco = None

# 3. Exibição do resultado
print("-" * 30)
if preco is not None:
    print(f"O preço do CD com selo {cor.capitalize()} é: R$ {preco:.2f}")
else:
    print("Erro: Cor inválida. Por favor, escolha uma cor da tabela.")
print("-" * 30)