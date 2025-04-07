nome = str(input("Nome de Usuario: "))
senha = str(input("Senha: "))

def digaoi():
    print(f"olá {nome}!")

if senha != "Senha123":
    while True:
        print("Invasor detectado!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

digaoi()