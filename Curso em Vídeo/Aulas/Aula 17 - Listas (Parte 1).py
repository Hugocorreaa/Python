'''



lanche = ()     - Tupla (No python novo se pode criar uma tupla sem parêntesis)
lanche = []     - Lista
lanche = {}     - Dicionário

-> Listas

São mutáveis!

Ex1
--Mudar elementos--

lanche = ['hamburguer', 'refrigerante', 'pizza', 'pudim']
lanche[3] = 'picolé'

# O valor 3 agora mudará para picolé.

lanche = ['hamburguer', 'refrigerante', 'pizza', 'picolé']


Ex2
--Adicionar elementos no final da lista--

lanche = ['hamburguer', 'refrigerante', 'pizza', 'picolé']
lanche.append('cookie)


Ex3
--Adicionar elementos em outras posições--

lanche = ['hamburguer', 'refrigerante', 'pizza', 'picolé', 'cookie']
lanche.insert(0,'hotdog')

lanche = ['hotdog', 'hamburguer', 'refrigerante', 'pizza', 'picolé', 'cookie']


Ex4
--Eliminar elementos--

lanche = ['hotdog', 'hamburguer', 'refrigerante', 'pizza', 'picolé', 'cookie']

del lanche[3]

#ou

lanche.pop(3)
lanche.pop() (irá eliminar o ultimo elemento)

#ou

lanche.remove('pizza')  # Remove remove o primeiro elemento encontrado na lista

lanche = ['hotdog', 'hamburguer', 'refrigerante', 'picolé', 'cookie']


Ex5

lanche = ['hotdog', 'hamburguer', 'refrigerante', 'pizza', 'picolé', 'cookie']
if 'pizza' in lanche:
    lanche.remove('pizza')


Ex6

valores = list(range(4,11))
# Faz uma contagem de 4 até 10 e colocará tudo dentro da variável 'valores' -> 4 5 6 7 8 9 10
valores = [4, 5, 6, 7, 8, 9, 10]


Ex7
--Ordenar elementos em valor do menor para o maior--

valores = [8, 2, 5, 4, 9, 3, 0]
valores.sort()
valores = [0, 2, 3, 4, 5, 8, 9]


Ex8
--Ordenar elementos do maior para menor--

valores = [8, 2, 5, 4, 9, 3, 0]
valores.sort(reverse=True)
valores = [9, 8, 5, 4, 3, 2, 0]


Ex9
--Saber o tamanho da lista--
# Quantos elementos tem?

valores = [0, 2, 3, 4, 5, 8, 9]
len(valores)
# valores tem 7 elementos


Ex10

valores = list()  # criando lista vazia
valores.append(5)
valores.append(9)
valores.append(4)

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')

        # Na posição 0 encontrei o valor 5!
        # Na posição 1 encontrei o valor 9!
        # Na posição 2 encontrei o valor 4!
        # Cheguei ao final da lista.


Ex11

valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')

# Digite um valor: 4
# Digite um valor: 8
# Digite um valor: 9
# Digite um valor: 1
# Digite um valor: 3
# Na posição 0 encontrei o valor 4!
# Na posição 1 encontrei o valor 8!
# Na posição 2 encontrei o valor 9!
# Na posição 3 encontrei o valor 1!
# Na posição 4 encontrei o valor 3!
# Cheguei ao final da lista.


Ex12
--Criando ligação de listas--

a = [2, 3, 4, 7]
b = a                   # Fazendo uma ligação entre listas.
b[2] = 8                # Se eu mundo um elemento da lista, também irá mudar na ligação
print(f'Lista A: {a}')
print(f'Lista B: {b}')


Ex13
--Criando cópia de listas--

a = [2, 3, 4, 7]
b = a[:]          # b recebe todos os itens de a.
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
'''

a = [2, 3, 4, 7]
b = a[:]          # b recebe todos os itens de a.
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
