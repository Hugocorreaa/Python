'''

Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
No final, mostre:

A) Quantas pessoas tem mais de 18 anos.
B) Quantos homens foram cadastrados.
C) Quantas mulheres tem menos de 20 anos.

'''

mais18 = homens = mulheresmenos20 = 0
while True:
    print('-' * 25)
    print('CADASTRE UMA PESSOA')
    print('-' * 25)

    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'mf':
        sexo = str(input('Sexo: [M/F] ')).strip().lower()[0]
    print('-' * 25)

    if idade >= 18:
        mais18 += 1
    if sexo == 'm':
        homens += 1
    if sexo == 'f' and idade < 20:
        mulheresmenos20 += 1

    continuar = ' '
    while continuar not in 'sn':
        continuar = str(input('Deseja continuar? [S/N] ')).strip().lower()[0]
    if continuar == 'n':
        break
print(f'O total de pessoas com mais de 18 anos: {mais18}')
print(f'Ao todo temos {homens} homens cadastrados.')
print(f'E temos {mulheresmenos20} mulheres com menos de 20 anos.')
