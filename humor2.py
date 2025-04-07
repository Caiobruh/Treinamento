from textblob import TextBlob

def pla(texto):
    humor = TextBlob(texto).sentiment.polarity
    if humor > 0.01:
        return "Positivo"
    elif humor < 0.01:
        return "Negativo"
    else:
        return "Neutro"

def linha(texto):
    frases = texto.split(".")
    for frase in frases:
        frase = frase.strip()
        if frase:
            print(f"frase:{frase}")
            print("humor detectado:",pla(frase))
            print()
ex = """
Every day brings new opportunities, and even in moments of frustration, growth is possible. You have incredible strength within you, and with determination, you can tackle any challenge that comes your way. Stay optimistic—your efforts will lead to great things!
"""
linha(ex)
pla(ex)