from random import randint
CPU = randint(1,3)
print('''------Escolha------
1. pedra💎
2. papel🧻
3. tesoura✂''')
ppt = int(input("Escolha: "))
print(f"a CPU escolheu : {CPU}")
if ppt == CPU:
    print("Empate!")
elif (ppt == 1 and CPU == 3) or \
    (ppt == 2 and CPU == 1) or \
    (ppt == 3 and CPU == 2):
    print("Voce venceu!")
else:
    print("Voce perdeu")
