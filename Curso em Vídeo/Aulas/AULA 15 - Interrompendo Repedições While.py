'''

n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s = s + n
#print('A soma vale {}'.format(s))
print(f'A soma vale {s}')

'''

nome = 'José'
idade = 33
salario = 987.3
print(f'O {nome} tem {idade:^20} anos e ganha R${salario:.2f}') # idade:^20 -> centralizou idade em 20 espaços
print(f'O {nome:<20} e maria')                      # Formatar à direita
print(f'O {nome:>20} e maria')                      # Formatar à esquerda
print(f'O {nome:-<10} e maria')
print(f'O {nome} tem {idade} anos.')                # PYTHON 3.6+
print('O {} tem {} anos.'.format(nome, idade))      # PYTHON 3

