'''

Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
No final, mostre uma listagem de preços, organizando os dados em forma tabular.

'''

produtos = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.00, 'Estojo', 25.00, 'Transferidor', 4.20,
            'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)

for pos in range(0, len(produtos)):
    if pos % 2 == 0:                         # Escolhe os pares. Na lista os pares são os produtos. print(produtos[0])
        print(f'{produtos[pos]:.<30}', end='')
    else:                                    # Escolha os ímpares. Na lista os ímpares são os preços. print(produtos[1])
        print(f'R${produtos[pos]:>7.2f}')
