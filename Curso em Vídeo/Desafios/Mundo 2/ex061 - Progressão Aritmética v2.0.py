'''
Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando
os 10 primeiros termos da progressão usando a estrutura while.

'''

print("=-=" * 10)
print("Gerador de PA")
print("=-=" * 10)

p = int(input('Primeiro termo: '))
r = int(input('Razão: '))

pa = p + (10 - 1) * r

termos = p
while termos <= pa:
    print(termos, end=" -> ")
    termos += r
print("FIM")
