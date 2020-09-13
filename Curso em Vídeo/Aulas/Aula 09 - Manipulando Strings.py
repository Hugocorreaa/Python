"""
    MANIPULANDO STRINGS

--> Cadeia de Caracteres (String)

"Curso em Vídeo Python"

Ao atribuir uma string à uma variável ela é indexada:

frase = "Curso em Vídeo Python"

[C][u][r][s][o] [] [e][m] [] [V][í][d][e][o] [] [P][y][t][h][o][n]
 0  1  2  3  4  5   6  7  8   9 10 11 12 13  14 15 16 17 18 19 20

21 caracteres

--> Fatiamento (Funcionalidade)

Ex1.

print(frase[9])
*EXECUTAR*
V                # Irá mostrar a 10ª letra.

******************************************************

Ex2.

print(frase[9:13])
*EXECUTAR*
Víde             # Começará do 9 e irá até o 12. O ultimo número, no caso 13, é sempre desconsiderado.

*******************************************************

Ex3.

print(frase[9:21])
*EXECUTAR*
Vídeo Python

********************************************************

Ex4.

print(frase[9:21:2])
*EXECUTAR*
VdoPto            # Começará no 9, vai até o 21, pulando de 2 em 2

*********************************************************

Ex5.

print(frase[:5])
*EXECUTAR*
Curso             # Quando o primeiro é omitido, ele sempre partirá da origem até onde é pedido, no caso 5.

**********************************************************

Ex6.

print(frase[15:])
*EXECUTAR*
Python            # Quando o segundo é omitido, ele partirá de onde é pedido, no caso 15, até o final.

***********************************************************

Ex7.

print(frase[9::3]
*EXECUTAR*
VePh             # Começa no 9 e vai até o final, pulando de 3 em 3.

************************************************************

--> Análise (Funcionalidade)

len(frase)              --> length = comprimento. Conta a quantidade de caracteres.
(21 caracteres)

frase.count("o")        --> Conta quantas vezes aparece o "o" minúsculo.
(3)

frase.count("o", 0, 13) --> Contagem com fatiamento
(1)                     # Vai considerar do 0 até o 13. Ou seja, existe somente um "o" do caracter do 0 ao 12

frase.find("deo")       --> Vai procurar onde começa a frase desejada
(11)                    # Encontrou "deo" na posição 11

frase.find("Android")   -->
(-1)                    # Irá retornar -1 porque a string "Android" não existe em frase.

"Curso" in frase        --> "Dentro de frase existe a string "Curso"?
(True)


--> Transformação (Funcionalidade)

Uma lista de string é imutável, porém é possivel mudar a partir de métodos.


frase.replace("Python", Android") --> Onde tiver "Python", ele irá substituir por "Android"

frase.upper()                     --> Transformará a string toda em MAIÚSCULO

frase.lower()                     --> Transformará a string toda em MINÚSCULO

frase.capitalize()                --> Transformará todos os caracteres para minúsculo e somente o primeiro caracter se transformará em maiúsculo

frase.title()                     --> Vai analisar quantas palavras tem a string pelo espaços e irá capitalizar o primeiro caracter pós o espaço

frase.strip()                     --> Irá remover os espaços do início e do fim

frase.rstrip()                    --> Irá remover os espaços da direita (right)

frase.lstrip()                    --> Irá remover os espaços da esquerda (left)


--> Divisão (Funcionalidade)

frase.split()                     --> Irá dividir e listar cada string a partir do espaço

|[C][u][r][s][o]|  |[e][m]|   |[V][[í][d][e][o]|  | [P][y][t][h][o][n] |
| 0  1  2  3  4 |  | 0  1 |   |0   1  2  3  4  |  | 0  1  2  3  4  5   |
|_______________|  |______|   |________________|  |____________________|
        0             1               2                      3


--> Junção (Funcionalidade)

"-".join(frase)                   --> Irá juntar as strings listadas separadas por "-"
(Curso-em-Vídeo-Python)




"""