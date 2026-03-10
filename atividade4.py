import os
os.system

# 1. Entrada de dados
renda_mensal = float(input("Digite a renda mensal: R$ "))
valor_total_solicitado = float(input("Digite o valor total do empréstimo: R$ "))
num_prestacoes = int(input("Digite em quantas parcelas deseja pagar: "))

# 2. Cálculos de Regra de Negócio
limite_total_emprestimo = renda_mensal * 10
valor_da_prestacao = valor_total_solicitado / num_prestacoes
limite_mensal_prestacao = renda_mensal * 0.30

# 3. Verificação dos Critérios (Ambos devem ser verdadeiros)
print("\n" + "="*30)
print("RELATÓRIO DE ANÁLISE")
print("="*30)

# Condição 1: Valor total <= 10x a renda
# Condição 2: Prestação <= 30% da renda
if valor_total_solicitado <= limite_total_emprestimo and valor_da_prestacao <= limite_mensal_prestacao:
    print("STATUS: EMPRÉSTIMO CONCEDIDO")
    print(f"Valor da Parcela: R$ {valor_da_prestacao:.2f}")
else:
    print("STATUS: EMPRÉSTIMO NEGADO")
    
    # Exibe o motivo específico para ajudar o usuário
    if valor_total_solicitado > limite_total_emprestimo:
        print(f"- O valor total excede o limite de R$ {limite_total_emprestimo:.2f}")
    if valor_da_prestacao > limite_mensal_prestacao:
        print(f"- A parcela de R$ {valor_da_prestacao:.2f} excede 30% da sua renda (R$ {limite_mensal_prestacao:.2f})")

print("="*30)