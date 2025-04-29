#desbloqueador de senhas(funciona com a NASA)
import time
from time import sleep
import getpass

print("quebrador de senhas")
print("começando...")

senha = getpass.getpass("qual a senha de 6 digitos? ")
if not senha.isdigit() or len(senha)!=6:
    print("erro, digite novamente.")
max = 1000
print("tentativa maxima permitida é ",max)

tempo = time.time()
encontrou = False
for tentativa in range(max):
    zeros = str(tentativa).zfill(6)
    #preenche com n de zeros
    print("acessando a senha...",zeros)
    sleep(0.000001)
    if zeros == senha:
        print("acesso liberado",senha)
        encontrou = True
        break
fim = time.time()
if not encontrou:
    print("nao e possivel encontrar a senha")
else:
    print("\ntempo de execuçao: ",round(fim - tempo))
    print("sistema invadido")