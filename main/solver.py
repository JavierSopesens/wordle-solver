from Dictionary import Dictionary
from userInterface import getMatches
from time import time
WORD_LENGTH = 5
DICTIONARY_FILE = 'es.txt'

myDict = Dictionary(DICTIONARY_FILE, WORD_LENGTH)
attempts = 0


def controlDuplicated(matches: list) -> list:
    # BUEN INTENTO, HACE FALTA ARREGLAR.
    # NO PODEMOS ELIMINAR EL ELEMENTO PORQUE SE PIERDE EL INDICE, CREANDO MALFUNCIONAMIENTOS
    # HAY QUE CONVERTIR EL VALOR DEL ELEMENTO EN '-' PARA QUE NO ENTRE EN LOS VALORES DE LA FUNCION REDUCE LIST DE LA CLASE DICCIONARY
    sorted_matches = sorted(matches, key=lambda x: ord(x[0]))
    anterior = sorted_matches[0]
    for elemento in sorted_matches[1:]:
        if elemento[0] == anterior[0]:
            if elemento[1] == '0' and anterior[1] == '0':
                matches.pop(matches.index(anterior))
                print(f'eliminem totes les {anterior[0]}')
            if elemento[1] == '0' and anterior[1] != '0':
                matches.pop(matches.index(elemento))
                print(f'eliminem totes les {elemento[0]}')
            if elemento[1] != '0' and anterior[1] == '0':
                matches.pop(matches.index(anterior))
                print(f'eliminem totes les {anterior[0]}')
        anterior = elemento
    return matches


# loop game
while len(myDict.words) != 1 and attempts != 5:
    print(f'remaining possible words: {len(myDict.words)}')
    print(myDict.words)
    matches = getMatches()

    # si en la lista hay dos letras iguales y una es un 0, no la pases
    matches = controlDuplicated(matches)
    print(matches)
    for index, match in enumerate(matches):
        myDict.reduceList(match[0], int(match[1]), index)
    # mientras no esté hecho el modulo de sugerencia, hacer un print de las words
    # TODO suggestions module
    # TODO analisis repeated letters. si la palabra a buscar es audio y uso avala,
    # recibire un valor de 20000. lo cual borrara todos los elementos de la lista
    #   pero no dejara de funcionar
    # testeo de funciones de userInterface y de nuevas funciones de la clase dictionary
    # control de errores si la lista esta vacia
    attempts += 1
