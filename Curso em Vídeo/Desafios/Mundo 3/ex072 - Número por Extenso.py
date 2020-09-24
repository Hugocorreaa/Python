'''

Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero
até vinte.

Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

'''

contagem = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze',
            'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

while True:
    escolha = int(input('Escolha um número de 0 a 20: '))
    if 0 <= escolha <= 20:
        print(f'Você digitou o número {contagem[escolha]}.')
        print('-' * 50)
        continuar = str(input('Você quer continuar? [S/N] ')).strip().lower()[0]
        print('-' * 50)
        if continuar == 'n':
            break
    else:
        print('Tente novamente.', end=' ')






