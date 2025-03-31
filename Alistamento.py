from datetime import date

ano = date.today().year
idade = int(input("qual o seu ano de nascimento? "))
dif = ano - idade
a = dif - 18
b = abs(a)
if dif == 18:
    print("parabens, esta na hora de alistar")
if dif > 18:
    print(f"Voce esta atrasado {b} anos para o alistamento")
if dif < 18:
    print(f"Voce esta adiantado, volte aqui daqui a {b} anos")