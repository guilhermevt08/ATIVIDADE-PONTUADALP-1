import os
os.system("cls || clear")

# 1. Entrada do código de operação
operacao = input("Digite a operação (+, -, * ou /): ")

# 2. Entrada dos valores inteiros
a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))

# 3. Processamento da operação escolhida
if operacao == '+':
    resultado = a + b
    simbolo = "Soma"
elif operacao == '-':
    resultado = a - b
    simbolo = "Subtração"
elif operacao == '*':
    resultado = a * b
    simbolo = "Multiplicação"
elif operacao == '/':
    # Verificação para evitar divisão por zero
    if b != 0:
        resultado = a / b
        simbolo = "Divisão"
    else:
        resultado = "Erro (Divisão por zero)"
        simbolo = "Divisão"
else:
    resultado = "Operação Inválida"
    simbolo = "Erro"

# 4. Exibição do resultado
print("-" * 30)
print(f"Operação: {simbolo}")
print(f"O resultado de {a} {operacao} {b} é: {resultado}")