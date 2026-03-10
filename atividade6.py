import os
os.system

# 1. Entrada das notas (usamos float para permitir casas decimais como 7.5)
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

# 2. Cálculo da média aritmética
media = (nota1 + nota2) / 2

# 3. Exibição da média
print("-" * 30)
print(f"Média Final: {media:.1f}") # O :.1f arredonda para 1 casa decimal

# 4. Estrutura de decisão para a situação do aluno
if media >= 6.0:
    print("Parabéns! Você está APROVADO.")
elif media >= 4.0:
    print("Você está em RECUPERAÇÃO.")
else:
    print("Infelizmente, você está REPROVADO.")
print("-" * 30)