a = 1
b = 0
semnasguardar = int(input("Quantas semanas vc quer guardar o din din? "))

while a != semnasguardar + 1:
    semana = int(input(f"Na semana {a} quanto voce vai guardar? "))
    a = a + 1
    b = b + semana
print(f"Total: {b}")
c = str(input("deseja fazer uma simulação de rendimento? s/n: "))
if c == "s":
    d = b * 1.01
    print(f"seu saldo total foi de {d}")