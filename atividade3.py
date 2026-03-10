import os
os.system("cls || clear")

# 1. Entrada de dados
# Usamos int() para garantir que os valores sejam tratados como números inteiros
a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))

# 2. Processamento da Lógica
if a == b:
    # Se forem iguais, soma
    c = a + b
    operacao = "soma"
else:
    # Caso contrário, multiplica
    c = a * b
    operacao = "multiplicação"

# 3. Saída de dados
print("-" * 20)
print(f"Resultado da {operacao}: {c}")