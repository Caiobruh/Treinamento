print("Olá, tudo bem? Como você esta hoje?")
print("----Emoções----")
print("1. Feliz")
print("2. Triste")
print("3. Medo")
print("4. Ansioso")
print("5. Tedio")
print("6. Vergonha")
print(("---------------"))
emocao = int(input("Qual é a sua emoção? "))

if emocao == 1:
    sla = str(input("Que bom que voce esta feliz! Me conte o porque"))
    print("Ohh que legal! A alegria está na luta, na tentativa, no sofrimento envolvido e não na vitória propriamente dita!")
elif emocao == 2:
    print("Que ruim... Fique tranquilo pois tenha coragem de enfrentar esse momento de tristeza e não deixe que ele dure mais do que deveria.")
elif emocao == 3:
    print("Que ruim, mas se lembre que o sucesso está do outro lado do medo.")
elif emocao == 4:
    print("Ser ansioso é imaginar uma tempestade antes da primeira gota d’água. Tente evitar se preocupar o que está longe de acontecer. A ansiedade é tenta lutar contra a calmaria do nosso coração. Não deixe que isto aconteça. Proteja-o de sofrimentos desnecessários.")
elif emocao == 5:
    print("O tédio é a doença dos corações sem sentimentos e das almas pobres. Arrume algo para fazer.")
elif emocao == 6:
    print("A vergonha é um reflexo das expectativas dos outros; seja gentil consigo mesmo.")
else:
    print("¯\_(ツ)_/¯  sla")