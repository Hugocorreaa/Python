# Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua área e a quantidade de tinta
# necessária para pintá-la. Sabendo que cada litro de tinta pinta uma área de 2m²

largura = float(input("Qual a largura da parede? "))
altura = float(input("Qual a altura da parede? "))
area = largura * altura
pintar = area / 2

print("Sua parede tem dimensão de {}x{} e sua área tem o valor de {}m².".format(largura, altura, area))
print("Para pintar uma parede de {}m² será necessário {}L de tinta.".format(area, pintar))
