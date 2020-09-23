'''
---> VARIÁVEIS COMPOSTAS <---

* Tuplas
* Listas
* Dicionários

lanche = ()     - Tupla (No python novo se pode criar uma tupla sem parêntesis)
lanche = []     - Lista
lanche = {}     - Dicionário

-> Tupla

As tuplas são IMUTÁVEIS!

lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
print(lanche)           # ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
print(lanche[1])        # 'Suco'
print(lanche[3])        # 'Pudim'
print(lanche[-2])       # 'Pizza'
print(lanche[1:3])      # 'Suco', 'Pizza'
print(lanche[2:])       # 'Pizza', 'Pudim'
print((lanche[:2]))     # 'Hambúrguer', 'Suco'
print(lanche[-2:])      # 'Pizza', Pudim
print(lanche[-3:])      # 'Suco', 'Pizza', 'Pudim'

Ex1.

lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
for comida in lanche:
    print(f'Eu vou comer {comida}.')
print('Comi pra caramba!')
                        # Eu vou comer Hambúrguer.
                        # Eu vou comer Suco.
                        # Eu vou comer Pizza.
                        # Eu vou comer Pudim.
                        # Comi pra caramba!

Ex2.

lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
print(len(lanche))
                        # 4

Ex3.

lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
for cont in range(0, len(lanche)):
    print(cont)
                        # 0
                        # 1
                        # 2
                        # 3
                        # 4

Ex4.

lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
for cont in range(0, len(lanche)):
    print(lanche[cont])
                        # Hambúrguer
                        # Suco
                        # Pizza
                        # Pudim
                        # Batata Frita

Ex5.

lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}')
                        # Eu vou comer Hambúrguer.
                        # Eu vou comer Suco.
                        # Eu vou comer Pizza.
                        # Eu vou comer Pudim.
                        # Eu vou comer Batata Frita.

Ex6.

lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}ª.')
                        # Eu vou comer Hambúrguer na posição 0ª
                        # Eu vou comer Suco na posição 1ª
                        # Eu vou comer Pizza na posição 2ª
                        # Eu vou comer Pudim na posição 3ª
                        # Eu vou comer Batata Frita na posição 4ª

Ex7.

lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}ª')
                        # Eu vou comer Hambúrguer na posição 0ª
                        # Eu vou comer Suco na posição 1ª
                        # Eu vou comer Pizza na posição 2ª
                        # Eu vou comer Pudim na posição 3ª
                        # Eu vou comer Batata Frita na posição 4ª


Ex8.

lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
print(sorted(lanche))
                        # ['Batata Frita', 'Hambúrguer', 'Pizza', 'Pudim', 'Suco']

                        # sorted coloca em ordem alfabética e transforma a tupla em lista.


Ex9.

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b

print(a)
print(b)
print(c)
                        # (2, 5, 4)
                        # (5, 8, 1, 2)
                        # (2, 5, 4, 5, 8, 1, 2)

Ex9.

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a

print(len(c))
print(c.count(5))
                        # 7
                        # 2

                        # .count(5) vai contar quantas vezes o 5 aparece

Ex10.

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a

print(c)
print(c.index(8))
                        # (5, 8, 1, 2, 2, 5, 4)
                        # 1

                        # .index(8) irá mostrar em qual posição o 8 está

Ex11.

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a

print(c)
print(c.index(5))

                        # (5, 8, 1, 2, 2, 5, 4)
                        # 0

                        # Porém temos dois 5. Ele irá mostrar a primeira ocorrência.

Ex12.

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a

print(c)
print(c.index(5, 1))
                        # (5, 8, 1, 2, 2, 5, 4)
                        # 4

                        # Ou seja, a partir da posição 1 ele irá procurar outro 5, já que na posição 0 temos o primeiro

Ex13.

pessoa = ('Gustavo', 39, 'M', 99.88)
print(pessoa)
                        # ('Gustavo', 39, 'M', 99.88)

Ex14. Deletar de tupla

pessoa = ('Gustavo', 39, 'M', 99.88)
del pessoa
print(pessoa)
                        # NameError: name 'pessoa' is not defined

'''


