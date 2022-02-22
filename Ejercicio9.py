"""Búsqueda de palabras en un diccionario
Sea una tabla de PALABRAS en español. Las palabras se guardan en una tabla llamada diccionario. Se utilizan otras dos tablas para recorrer el diccionario. Para cada palabra, una tabla llamada siguiente da el número de la celda ocupada por la palabra que le sigue en orden alfabético en el diccionario. La tabla anterior también da, para cada palabra, el número de la celda del diccionario que contiene la palabra anterior en orden alfabético. A la primera palabra de la lista ordenada le corresponde un número de celda del anterior igual a índice_min(diccionario) - 1. Igualmente, a la última palabra de la lista ordenada le corresponde un número de celda de la siguiente igual al mismo valor. La tabla que aparece debajo muestra un ejemplo de estas tres tablas.
i     diccionario      anterior     siguiente
1     avión               3             4
2     tren                4            ...
3     auto                0             1
4     camión              1             2
5     ...                ...           ...
Se ve que para ‘camión’, en la celda 4, la palabra siguiente en orden alfabético ocupa la celda 2 y la anterior ocupa la celda 1. Entonces, el orden alfabético de estas tres palabras es ‘avión’, ‘camión’ y ‘tren’.
1. Escribir el algoritmo que da la lista de las palabras guardadas empezando por una letra dada.
Así, por ejemplo, el algoritmo aplicado a la lista anterior dará (‘avión’, ‘auto’) para la letra ’a’.
También es posible definir un tipo nuevo de datos, PALABRA, formado con una cadena de caracteres para la palabra propiamente dicha y con dos números enteros para descubrir la palabra anterior y la siguiente en el diccionario. En este caso, el diccionario se convierte en una simple tabla de PALABRAS.
2. Definir el tipo PALABRA y rehacer el algoritmo anterior para utilizarlo.
3. Escribir el algoritmo que permite añadir una palabra nueva al diccionario.
4. Escribir el algoritmo de eliminación de una palabra."""
def ordenarClaves():
  dict={"avion":1,"tren":2,"auto":3,"camion":4}
  for key in sorted(dict.keys()) :
    print(key , ":" , dict[key])
  dict[5] = "moto"
  dict.pop("camion")
  return print(dict)