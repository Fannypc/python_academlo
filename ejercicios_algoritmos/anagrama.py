def anagrama(palabras):
    try:
        palabras = palabras.split() #n
        palabra_1 = palabras[0]
        palabra_2 = palabras[1]
    except:
        return('Error')

    if palabra_1 == palabra_2:
        return('Las palabras son iguales')

    if len(palabra_1) != len(palabra_2):
        return ('Las palabras no tienen la misma longitud')

    primera=list(palabra_1)
    segunda=list(palabra_2)
    primera.sort() #n2
    segunda.sort() #n2

    if primera == segunda:
        return('Son anagramas')
    else:
        return('No son anagramas')


while(True):
    print(anagrama(input('Ingresa las dos palabras separadas por un espacio: \n')))
