#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
Ganha_h = int(input("Opa, o quanto você ganha por hora? "))
Numer_h = int(input("Opa quantas horas você trabalha por dia? "))

cal = Ganha_h*(Numer_h*30)

print("Então você ganha: " + str(cal))
