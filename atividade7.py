import os
os.system

# 1. Entrada de dados
nome_produto = input("Digite a descrição do produto (nome): ")
quantidade = int(input(f"Digite a quantidade de {nome_produto} adquirida: "))
preco_unitario = float(input("Digite o preço unitário: R$ "))

# 2. Cálculo do total bruto
total_bruto = quantidade * preco_unitario

# 3. Definição do percentual de desconto
if quantidade <= 5:
    percentual_desconto = 0.02  # 2%
elif quantidade <= 10:
    percentual_desconto = 0.03  # 3%
else:
    percentual_desconto = 0.05  # 5%

# 4. Cálculos finais
valor_desconto = total_bruto * percentual_desconto
total_a_pagar = total_bruto - valor_desconto

# 5. Exibição dos resultados
print("-" * 40)
print(f"Produto: {nome_produto}")
print(f"Total Bruto: R$ {total_bruto:.2f}")
print(f"Desconto aplicado ({percentual_desconto*100:.0f}%): R$ {valor_desconto:.2f}")
print(f"Total a Pagar: R$ {total_a_pagar:.2f}")
print("-" * 40)