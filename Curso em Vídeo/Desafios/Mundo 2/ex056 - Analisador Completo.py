"""
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:

-> A média de idade do grupo.
-> Qual é o nome do homem mais velho.
-> Quantas mulheres tem menos de 20 anos.

"""

n_h_velho = ""             #Nome_homem_velho
h_velho = 0                #Homem_velho
m_men_20 = 0               #Mulher_menor_20anos
soma_idade = 0
media = soma_idade / 4

for c in range(1, 5):
    print("----- {}ª PESSOA -----".format(c))
    nome = (input("Nome: ".format(c))).strip().capitalize()
    idade = int(input("Idade: ".format(c)))
    sexo = (input("Sexo [M/F]: ".format(c))).lower().strip()

    soma_idade += + idade

    if sexo == "f" and idade < 20:
        m_men_20 += 1
    if sexo == "m":
        if idade > h_velho:
            h_velho = idade
            n_h_velho = nome

print("\nA média de idade do grupo é de {:.1f} anos.".format(media))
print("O homem com idade mais velha tem {} anos e seu nome é {}.".format(h_velho, n_h_velho))
print("Há {:.0f} mulheres com menos de 20 anos.".format(m_men_20))
