"""
Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos
dessa progressão.

"""

print("-=-" * 13)
print("   10 PRIMEIROS TERMOS DE UMA PA")
print("-=-" * 13)

primeiro = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))

n = primeiro + (10 - 1) * razao
for c in range(primeiro, n + 1, razao):
    print(c, end=" -> ")
print("FIM")

# Temos que criar um laço que mostre os números que vão desde o primeiro, até o décimo termo alternando com o valor da
# razão. Para saber o décimo termo, teremos que calcular antes com a fórmula, para assim colocar no laço.
