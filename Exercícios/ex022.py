#Crie um programa que leia o nome completo de uma pessoa e mostre:
#– O nome com todas as letras maiúsculas e minúsculas.
#– Quantas letras ao t'odo (sem considerar espaços).
#– Quantas letras tem o primeiro nome.

nome = str(input("Qual o seu nome completo? ")).strip()
print("Seu nome em maiúsculas é", nome.upper())
print("Seu nome em minúsculas é", nome.lower())

nome_separado = nome.split()
print("Seu nome tem ao todo", len("".join(nome_separado)), "letras")

print("Seu primeiro nome é", nome_separado[0], "e ele tem", len(nome_separado[0]), "letras")

#Outra maneira de fazer:

print("Seu nome em maiúsculas é {}".format(nome.upper()))
print("Seu nome em minúsculas é {}".format(nome.lower()))

print("Seu nome tem ao todo {} letras".format(len(nome) - nome.count(" ")))
