#desbloqueador de senhas(funciona com a NASA)
import time
from time import sleep

print("quebrador de senhas")
print("começando...")

senha = input("qual a senha de 4 digitos? ")

tempo = time.time()
for tentativa in range(10000):
    zeros = str(tentativa).zfill(4)
    #preenche com n de zeros
    print("acessando a senha...",zeros)
    sleep(0.0001)
    if zeros == senha:
        print("acesso liberado",senha)
        break
fim = time.time()
print("\ntempo de execuçao: ",round(fim - tempo))
print("sistema invadido")