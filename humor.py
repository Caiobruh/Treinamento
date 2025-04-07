from textblob import TextBlob

def humor(texto):
    sla = TextBlob(texto).sentiment.polarity
        if sla > 0.01:
        return "Positivo"
    elif sla < 0.01:
        return "Negativo"
    else:
        return "Neutro"

ex = ("que bom")

print("Humor detectado",humor(ex))