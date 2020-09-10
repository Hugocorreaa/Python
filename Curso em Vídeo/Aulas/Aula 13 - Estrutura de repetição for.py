"""

---->  Laço de Repetição ou Iterações

for c in range(1, 6):
    print("Oi")
print("FIM")
*EXECUTANDO*
Oi
Oi
Oi
Oi
Oi
FIM


# "c" é uma variável qualquer. Nesse caso, c de "contador".
# Ele escreveu 5 vezes "Oi" porque de 1 até 6, ele vai fazer de 1 até 5 e no 6 ele irá parar.


for c in range(0, 6):
    print("Oi)
print("FIM"
*EXECUTANDO*
Oi
Oi
Oi
Oi
Oi
Oi
FIM


# Nesse caso ele escreve "Oi" 6 veze porque o 0 conta como 1. 0,1,2,3,4,5.
# Pode-se visualizar melhor no exemplo abaixo:


for c in range(0, 6):
    print(c)
print("FIM")
*EXECUTANDO*
0
1
2
3
4
5
FIM


# Outro Exemplo: Contagem de 1 até 6


for c in range(1, 7):       # Vai conta de 1 até 7 (1, 2, 3, 4, 5, 6). Lembre-se que o ultimo número não conta.
    print(c)
print("FIM)
*EXECUTANDO*
1
2
3
4
5
6
FIM



# Contagem regressiva:


for c in range(6, 0, -1):
    print(c)
print("FIM")
*EXECUTANDO*
6
5
4
3
2
1
FIM

# Nesse caso o -1 define a iteração.

# Outro Exemplo:


for c in range(0 , 7, 2):
    print(c)
print("FIM"
*EXECUTANDO*
0
2
4
6
FIM

# Nesse exemplo vemos que ao definir a iteração em 2, ele faz a contagem pulando de 2 em 2.

# Outro Exemplo:


n = int(input("Digite um número: "))
for c in range(0, n):
    print(c)
print("FIM")
*EXECUTANDO*
Digite um número: 10
0
1
2
3
4
5
6
7
8
9
FIM


# Para chegar no número exato do valor lido pelo input adicionaremos +1 ao n


n = int(input("Digite um número: "))
for c in range(0, n+1)
    print(c)
print("FIM")
*EXECUTANDO*
Digite um número: 10
0
1
2
3
4
5
6
7
8
9
10


# Outro Exemplo


i = int(input("Início: ")) # i -> início
f = int(input("Fim: "))    # f -> fim
p = int(input("Passo "))   # p -> passo
for c in range(i, f+1, p)
    print(c)
print("FIM")
*EXECUTANDO*
Início: 2
Fim: 9
Passo: 3
2
5
8
FIM

# Nesse exemplo a contagem irá de 2 até 9 de 3 em 3.

# Outro exemplo:



for c in range (0, 3):
    n = int(input("Digite um valor: "))
print("FIM")
*EXECUTANDO*
Digite um valor:
Digite um valor:
Digite um valor:
FIM

# Nesse exemplo a variável n será escrita 3 vezes (de 0 a 3 -> 0, 1, 2,)

# Somatório dos números


s = 0                                      # s -> somatório
for c in range(0, 4):                      # de 0 a 4 (0, 1, 2, 3)
    n = int(input("Digite um valor: '))
    s += n                                 # s = s + n
print("O somatório de todos os valores foi {}".format(s))
*EXECUTANDO*
Digite um valor: 4
Digite um valor: 2
Digite um valor: 3
Digite um valor: 1
O somatório de todos os valores foi 10     # Ele somou s = s + n (s = 0 + 4 = 4 -> s = 4 + 2 = 6 -> s = 6 + 3 = 9 ->
                                             s = 9 + 1 = 10)

"""