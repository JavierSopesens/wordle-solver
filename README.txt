Program to help you to play WORDLE in spanish

this folder contains:
    - 0.es.txt                  list of all the words in spanish
    - 1.read_doc.py             with the script to create and fill txt with only words with 5 characters
    - 2.five_char_words.txt     contains every word in spanish with 5 characters
    - 3.read_five_char_words.py to check the content of five_char_words.txt

NEXT STEPS
  - solucionar bug por el cual si una letra se repite la evaluará dos veces con resultados diferentes
    -si por ejemplo tenemos (cacan, 22000)(true story) 
      evaluara que solo pueden haber palabras con c y 
      evaluara que solo pueden haber palabras sin c
  - mejorar la forma en la que los datos son introducidos. Tener que alterar los valores del array dentro del documento es un rollo
  - control de variables
  - documento aconsejador de palabras:
    - recorrer el documento con las palabras
    - asignar un valor a cada letra en funcion de las veces que aparece en el documento
    - sumar los valores de cada letra de la palabra (la palabra pasa a tener un valor numérico)
    - mostrar las recomendaciones en funcion de su valor
    - priorizar mostrar palabras sin letras repetidas
