idade = int(input("Qual a sua idade? "))

def verificaridade():
    if idade >= 18:
        print("Você é maior de 18!")
    else:
        print("Você é menor de 18!")

verificaridade()