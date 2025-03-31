from datetime import date

ano =  date.today().year
nasc = int(input("qual o seu ano de nascimento? "))
idade = ano - nasc

if idade < 9:
    print("Voce foi qualificado para MIRIM")
elif idade < 14:
    print("Voce foi qualificado para INFANTIL")
elif idade < 19:
    print("Voce foi qualificado para JUNIOR")
elif idade < 25:
    print("Voce foi qualificado para SÊNIOR")
else:
    print("Voce foi qualificado para MASTER")