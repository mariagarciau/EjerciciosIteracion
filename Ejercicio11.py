"""mcd de dos números enteros
El algoritmo que permite determinar el máximo común divisor de dos números enteros también se estudia en el capítulo «Recursividad», durante el estudio del tipoFRACCIÓN. 
1. Dar una versión iterativa del algoritmo de Euclides para el cálculo del mcd de dos números enteros.
2. Estudiar una versión iterativa que calcula el mcd haciendo solo sumas o restas.
Puede encontrar una solución completa de este ejercicio en los complementos disponibles para descargar desde la página Información."""
def mcd(n1,n2):
  while n1%n2 != 0:
    resto=n1%n2
    n1=n2
    n2=resto
  return n2
print(mcd(20,4))