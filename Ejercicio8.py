"""Análisis de una cadena de caracteres
Sea una cadena de caracteres con distintas partes separadas por un carácter SEPARADOR específico. El ejemplo que aparece aquí debajo representa una cadena de este tipo, donde el carácter separador es dos puntos ’:’.
Este es un:ejemplo : de cadena a analizar: 
Se quieren separar las distintas partes y situarlas en una tabla de cadenas de caracteres. Para el ejemplo que aparece antes, se quiere obtener la tabla siguiente:

n.°        Cadena
1          ’Este es un’
2          ’ejemplo ’
3          ’ de cadena para analizar’
1. Escribir el módulo de software que realiza esta descomposición.
2. Utilizar este módulo en un algoritmo de búsqueda de los campos GCOS del archivo /etc/passwd de un sistema UNIX.
Se trata de construir una tabla que da todos los campos obtenidos asociados al identificador de un usuario. El algoritmo emite una alerta cuando el campo GCOS no se ha completado con la descripción del usuario.
"""
def cadenaCaracteres():
  cadena=input("Introduce una cadena: ")
  print(cadena.split(":"))

