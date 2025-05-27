# logica_braille.py

# Diccionario Braille con letras y caracteres especiales
braille_dict = {
    'a': [1,0,0,0,0,0], 'b': [1,1,0,0,0,0], 'c': [1,0,0,1,0,0],
    'd': [1,0,0,1,1,0], 'e': [1,0,0,0,1,0], 'f': [1,1,0,1,0,0],
    'g': [1,1,0,1,1,0], 'h': [1,1,0,0,1,0], 'i': [0,1,0,1,0,0],
    'j': [0,1,0,1,1,0], 'k': [1,0,1,0,0,0], 'l': [1,1,1,0,0,0],
    'm': [1,0,1,1,0,0], 'n': [1,0,1,1,1,0], 'o': [1,0,1,0,1,0],
    'p': [1,1,1,1,0,0], 'q': [1,1,1,1,1,0], 'r': [1,1,1,0,1,0],
    's': [0,1,1,1,0,0], 't': [0,1,1,1,1,0], 'u': [1,0,1,0,0,1],
    'v': [1,1,1,0,0,1], 'w': [0,1,0,1,1,1], 'x': [1,0,1,1,0,1],
    'y': [1,0,1,1,1,1], 'z': [1,0,1,0,1,1],
    'ñ': [1,1,0,0,1,1]  # símbolo propio para ñ
}

# Función que convierte texto a listas de celdas Braille (6 bits cada una)
def texto_a_braille(texto):
    texto = texto.lower()
    resultado = []
    for letra in texto:
        if letra in braille_dict:
            resultado.append(braille_dict[letra])
        elif letra in ['á','é','í','ó','ú']:
            resultado.append([0,1,1,0,0,1])  # signo de acento agudo ⠷
            resultado.append(braille_dict[letra.replace('á','a')
                                          .replace('é','e')
                                          .replace('í','i')
                                          .replace('ó','o')
                                          .replace('ú','u')])
        elif letra == 'ü':
            resultado.append([0,1,1,0,1,1])  # signo de diéresis ⠳
            resultado.append(braille_dict['u'])
        else:
            resultado.append([0,0,0,0,0,0])  # celda vacía para caracteres no reconocidos
    return resultado

# Función que genera una visualización estilo Braille con ● y ○
def render_braille_ascii(celdas):
    fila1, fila2, fila3 = "", "", ""
    for bits in celdas:
        f1 = ("●" if bits[0] else "○") + " " + ("●" if bits[3] else "○")
        f2 = ("●" if bits[1] else "○") + " " + ("●" if bits[4] else "○")
        f3 = ("●" if bits[2] else "○") + " " + ("●" if bits[5] else "○")
        fila1 += f1 + "   "
        fila2 += f2 + "   "
        fila3 += f3 + "   "
    return fila1 + "\n" + fila2 + "\n" + fila3
