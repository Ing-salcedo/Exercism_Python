def convert(numero):
    """Convierte un numero en una cadena de caracteres definida"""
    res = ''
    if numero % 3 == 0:
        res += 'Pling'
    if numero % 5 == 0:
        res += 'Plang'
    if numero % 7 == 0:
        res += 'Plong'
    return res or str(numero)
