import os
os.system("cls || clear")
# Entrada de dados 
a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))

# Cálculo da soma
soma = a + b

# Estrutura Condicional
if soma < c:
    print(f"A soma de A + B ({soma}) é menor que C ({c}).")
else:
    print(f"A soma de A + B ({soma}) é maior que C ({c}).")