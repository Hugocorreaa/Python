'''

Crie um programa onde o usuário possa digitar cinco valore numéricos e cadastre-os
em uma lista, já na posição correta de inserção (sem usar o sort()).

No final, mostre a lista ordenada na tela.

'''

valores = []

for c in range(0, 5):
    adicionar = int(input('Digite um valor: '))
    if c == 0 or adicionar > valores[-1]:
        valores.append(adicionar)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        teste = len(valores)
        while pos < teste:
            if adicionar <= valores[pos]:
                valores.insert(pos, adicionar)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
print(f'Os valores digitados foram {valores}')




