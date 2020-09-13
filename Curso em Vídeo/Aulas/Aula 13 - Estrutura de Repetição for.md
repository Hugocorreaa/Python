# ESTRUTURAS DE REPETIÇÕES

## **LAÇO DE REPETIÇÃO OU ITERAÇÕES**

```
for c in range("inicio", "fim","alternância"):
```

"c" é uma variável qualquer. Nesse caso, c de "contador".

"c" irá repetir do "iníco" ao "fim" alternando entre "alternância)

**Ex1.**
```
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
```
Foi escrito 5 vezes "Oi" porque, de 1 até 6, irá se repetir de 1 até 5 e no 6 ele irá parar.


**Ex2.**
```
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
```
Nesse caso se repetirá "Oi" 6 veze porque o 0 conta como 1 --> 0,1,2,3,4,5.


**Pode-se visualizar melhor no exemplo abaixo:**

**Ex3.**
```
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
```

**Ex4. Contagem de 1 até 6**
```
for c in range(1, 7):
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
```
Irá contar de 1 até 7 (1, 2, 3, 4, 5, 6). Lembre-se que o ultimo número não conta.

**Ex5.**
```
for c in range(0 , 7, 2):
    print(c)
print("FIM")
*EXECUTANDO*
0
2
4
6
FIM
```
Nesse exemplo vemos que ao definir a alternância em 2, ele faz a contagem pulando de 2 em 2.

**Ex6.**
```
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
```
Nesse exemplo a contagem irá de 2 até 9 de 3 em 3.

Lembre-se que para chegar no final exatado é necessário acrescentar +1 ao "fim" por isso ```f+1```.

**Ex7.**
```
for c in range (0, 3):
    n = int(input("Digite um valor: "))
print("FIM")
*EXECUTANDO*
Digite um valor:
Digite um valor:
Digite um valor:
FIM
```
Nesse exemplo a variável n será escrita 3 vezes (de 0 a 3 -> 0, 1, 2,)



### Contagem regressiva:
```
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
```
Nesse caso o -1 define a iteração.

**Ex8. Palavras Invertidas**
```
1.frase = str(input("Digite: ")).upper().strip().split()
2.junto = "".join(frase)
3.
4.for c in range(len(junto) - 1, -1, -1):
5.    print(junto[c], end="") 
6.*EXECUTAR*
7.Digite: roma
8.AMOR
9.

```
A linha 1 e 2 tiram os espaços da frase e a junta (Melhor entendendimento na [AULA 9 - Manipulação de strings](https://github.com/Hugocorreaa/Python/blob/master/Curso%20em%20V%C3%ADdeo/Aulas/Aula%2009%20-%20Manipulando%20Strings.md).

```4.for c in range(len(junto) - 1, -1, -1):```

A linha 4 define que "c" vai do ultimo caracter de ```junto``` (4-1=3), até o caracter 0, de modo invertido (ou seja, de 3 a 0)
```
print(len(junto))
*EXECUTAR*
4
```

--|  |  |--
--|--|--|--
R |O |M |A
0 |1 |2 |3

(4 caracteres)

### Somatório dos números

```
s = 0                                                        # s -> somatório
for c in range(0, 4):                                        # de 0 a 4 (0, 1, 2, 3)
    n = int(input("Digite um valor: '))
    s += n                                                   # s = s + n
print("O somatório de todos os valores foi {}".format(s))
*EXECUTANDO*
Digite um valor: 4
Digite um valor: 2
Digite um valor: 3
Digite um valor: 1
O somatório de todos os valores foi 10 
```
Ele somou s = s + n (s = 0 + 4 = 4 **->** s = 4 + 2 = 6 **->** s = 6 + 3 = 9 **->** s = 9 + 1 = 10)
