'''
Fala um programa que leia o sexo de uma pessoa, mas só aceita os valores 'M' ou 'F'.
Caso esteja errado, peça a digitação novamente até ter um valor correto.

'''

'''sexo = str(input('Informe seu sexo: [M/F] ')).lower().strip()
while sexo != "m" != "f":
    sexo = str(input("Operação incorreta. Por favor, informe seu sexo: "))
    if sexo == "m":
        print('Sexo masculino registrado com sucesso!')
    if sexo == "f":
        print('Sexo feminino registrado com sucesso!')'''


sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0] # [0] -> para pegar somente o primeiro carácter.
while sexo not in 'MF':
    sexo = str(input('Informação inválida. Por favor, informe seu sexo: ')).strip().upper()[0]
print("Sexo {} registrado com sucesso!".format(sexo))
