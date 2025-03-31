preconor = float(input("Insira o preço do produto: "))
precodps = 0
print("--------------Menu--------------")
print("1. á vista cheque/dinheiro: -10%")
print("2. A vista no cartão: -5%")
print("3. em ate 2x no cartao")
print("4. 3x ou mais no cartão: +20%")
print("--------------------------------")
opcao = int(input("Escolha a forma de pagamento: "))

if opcao == 1:
    precodps = preconor * 0.9
    print("-----------Conta-----------")
    print(f"preço: {preconor}")
    print(f"desconto: {preconor * 0.1}")
    print("---------------------------")
    print(f"Total: {precodps}")
elif opcao == 2:
    precodps = preconor * 0.95
    print("-----------Conta-----------")
    print(f"preço: {preconor}")
    print(f"desconto: {preconor * 0.05}")
    print("---------------------------")
    print(f"Total: {precodps}")
elif opcao == 3:
    precodps = preconor
    print("-----------Conta-----------")
    print(f"preço: {preconor}")
    print("---------------------------")
    print(f"Total: {precodps}")
elif opcao == 4:
    precodps = preconor * 1.2
    print("-----------Conta-----------")
    print(f"preço: {preconor}")
    print(f"Juros: {preconor * 0.2}")
    print("---------------------------")
    print(f"Total: {precodps}")
    print("Total {\:2f}".format(precodps))