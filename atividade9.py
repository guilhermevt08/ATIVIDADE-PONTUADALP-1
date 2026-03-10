import os
os.system

# 1. Entrada de dados
renda_mensal = float(input("Digite a renda mensal do solicitante: R$ "))
valor_emprestimo = float(input("Digite o valor total do empréstimo: R$ "))
num_prestacoes = int(input("Digite o número de prestações desejado: "))

# 2. Cálculos de referência
limite_total_emprestimo = renda_mensal * 10
valor_prestacao = valor_emprestimo / num_prestacoes
limite_prestacao = renda_mensal * 0.30

# 3. Verificação dos critérios
print("-" * 40)
print(f"Análise de Crédito:")
print(f"Valor da Prestação: R$ {valor_prestacao:.2f}")
print(f"Limite da Prestação (30% da renda): R$ {limite_prestacao:.2f}")

# A condição 'and' garante que os dois critérios sejam respeitados
if valor_emprestimo <= limite_total_emprestimo and valor_prestacao <= limite_prestacao:
    print("\nRESULTADO: Empréstimo CONCEDIDO!")
else:
    print("\nRESULTADO: Empréstimo NEGADO.")
    
    # Detalhando o motivo do erro (opcional, para ajudar o usuário)
    if valor_emprestimo > limite_total_emprestimo:
        print("- Motivo: O valor total excede 10x a renda mensal.")
    if valor_prestacao > limite_prestacao:
        print("- Motivo: A prestação compromete mais de 30% da renda.")
print("-" * 40)