import os
os.system("cls || clear")


# 1. Entrada de dados
litros = float(input("Digite o número de litros vendidos: "))
tipo = input("Digite o tipo de combustível (A-álcool, G-gasolina): ").strip().upper()

# 2. Definição de preços base
preco_gasolina = 6.59
preco_alcool = 3.79
valor_final = 0

# 3. Processamento da Lógica de Desconto
if tipo == 'A':
    # Lógica para Álcool
    if litros <= 20:
        percentual_desconto = 0.03
    else:
        percentual_desconto = 0.05
    valor_final = litros * (preco_alcool * (1 - percentual_desconto))

elif tipo == 'G':
    # Lógica para Gasolina
    if litros <= 20:
        percentual_desconto = 0.04
    else:
        percentual_desconto = 0.06
    valor_final = litros * (preco_gasolina * (1 - percentual_desconto))

else:
    print("Tipo de combustível inválido!")

# 4. Exibição do resultado
if valor_final > 0:
    print("-" * 35)
    print(f"Combustível: {'Álcool' if tipo == 'A' else 'Gasolina'}")
    print(f"Quantidade: {litros} litros")
    print(f"Total a pagar: R$ {valor_final:.2f}")
    print("-" * 35)