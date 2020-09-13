# MANIPULANDO STRINGS

## **CADEIA DE CARACTER OU STRING**

**Exemplo de string:** `"Curso em Vídeo Python"`

Toda string em python está entre " "

**Ao atribuir uma string à uma variável ela será indexada:**

`frase = "Curso em Vídeo Python"`

-- |0  |1  |2  |3  |4  |5  |6  |7  |8  |9  |10 |11 |12 |13 |14 |15 |16 |17 |18 |19 |20
---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---
-- |[C]|[u]|[r]|[s]|[o]|[ ]|[e]|[m]|[ ]|[V]|[í]|[d]|[e]|[o]|[ ]|[P]|[y]|[t]|[h]|[o]|[n]

A variável `frase` tem 21 caracteres, pois o 0 conta como o primeiro caracter.

**Outros exemplo de manipulação de strin:**

`frase[começo : fim : alternancia]`

Os exemplos estão na funcinalidade de Fatiamento.


## **-> FUNCIONALIDADES**

### - Análise

-- |   |   | Retorna
---|---|---| --
-> |len(frase)              |Conta a quantidade de caracteres a string tem. |(21)
-> |frase.count("o")        |Conta quantas vezes aparece o "o" minúsculo.   |(3)
-> |frase.count("o", 0, 13) |Contagem com fatiamento.                       |(1)
-> |frase.find("deo")       |Vai procurar onde começa a string "deo".       |(11)
-> |Curso" in frase         |Dentro de frase existe a string "Curso"?       |(True)


### - Transformação

Uma lista de string é imutável, porém é possivel mudar a partir de métodos.

-- |   |   | --
---|---|---| --
-> |frase.replace("Python", Android")      |Onde tiver "Python", ele irá substituir por "Android".
-> |frase.upper()                          |Transformará a string toda em MAIÚSCULO.
-> |frase.lower()                          |Transformará a string toda em MINÚSCULO.
-> |frase.strip()                          |Irá remover os espaços do início e do fim.
-> |frase.rstrip()                         |Irá remover os espaços da direita (right).
-> |frase.lstrip()                         |Irá remover os espaços da esquerda (left).
-> |frase.capitalize()                     |Transformará somente o primeiro caracter em maiúsculo.
-> |frase.title()                          |Irá capitalizar todo primeiro caracter pós espaço.
### - Divisão 

-- |   |   | --
---|---|---| --
-> | frase.split()                    |Irá dividir e listar cada string a partir do espaço

**Exemplo:**

`frase.split()`

-- |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | --
---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---
-- |[C]|[u]|[r]|[s]|[o]|   |[e]|[m]|   |[V]|[í]|[d]|[e]|[o]|   |[P]|[y]|[t]|[h]|[o]|[n]| --
-- |0  |1  |2  |3  |4  |   |0  |1  |   |0  |1  |2  |3  |4  |   |0  |1  |2  |3  |4  |5  | --

**[C] [u] [r] [s] [o]** = 0

**[e] [m]** = 1

**[V]|[í] [d] [e] [o]** = 2

**[P] [y] [t] [h] [o] [n]** = 3
### - Junção

-- |   |   | --
---|---|---| --
-> |"-".join(frase)                   | Irá juntar as strings listadas separadas por "-"
(Curso-em-Vídeo-Python)




### - Fatiamento

**Ex1.**
```
frase = Curso em Vídeo Python
print(frase[9])
*EXECUTAR*
V
```                  

Irá mostrar a 10ª letra ou 9º caracter.
***

**Ex2.**
```
frase = Curso em Vídeo Python
print(frase[9:13])
*EXECUTAR*
Víde            
```
Começará do 9º e irá até o 12º. O ultimo número, no caso 13, é sempre desconsiderado.
***

**Ex3.**
```
frase = Curso em Vídeo Python
print(frase[9:21])
*EXECUTAR*
Vídeo Python
```
***

**Ex4.**
```
frase = Curso em Vídeo Python
print(frase[9:21:2])
*EXECUTAR*
VdoPto            
```
Começará no 9, vai até o 21, pulando de 2 em 2
***

**Ex5.**
```
frase = Curso em Vídeo Python
print(frase[:5])
*EXECUTAR*
Curso            
```
Quando o primeiro é omitido, ele sempre partirá da origem até onde é pedido, no caso 5.

***
**Ex6.**
```
frase = Curso em Vídeo Python
print(frase[15:])
*EXECUTAR*
Python
```
Quando o segundo é omitido, ele partirá de onde é pedido, no caso 15, até o final.
***

**Ex7.**
```
print(frase[9::3])
*EXECUTAR*
VePh
```
Começa no 9 e vai até o final, pulando de 3 em 3.
***

## **-> OUTROS EXEMPLOS**

```
frase = "Curso em Vídeo Python"
print(frase[::-1])
*EXECUTAR*
nohtyP oedíV me osruC
```
