#Faça um programa que leia uma frase pelo teclado e mostre:
#-Quantas vezes aparece a letra "A".
#-Em que posição ela aparece a primeira vez.
#-Em que posição ela aparece a última vez.

frase = str(input("Digite uma frase: ")).strip().lower()
print("A letra 'a' aparece {} vezes".format(frase.count("a")))

print("Ela aparece pela primeira vez na posição {}".format(frase.find("a") + 1))

print("E ela aparece pela última vez na posição {}".format(frase.rfind("a") + 1))
