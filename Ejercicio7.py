"""Edición de un número entero
1. Escribir un algoritmo iterativo que transforme un número entero n cualquiera en su representación en una base B ≥ 2 cualquiera.
Cuando la base es superior a 36, se puede utilizar la representación de los números en base diez, pero separando cada cifra de la representación del número en base B mediante un separador convenido, por ejemplo, un punto. Eso es lo que se usa para expresar, por ejemplo, la dirección IP de un host en una red con IPv4. Así, por ejemplo, la representación en base 256 de 3000, expresada aquí en base diez, se escribirá: 11 184256 = 3000diez."""
def suma_de_control_acu(n, multiplicador, suma : int):
  n >= 0
  
  base : int = 10
  sumaMultiplicadores : int = 3
  if n < base:
    Resultado = suma + (n * multiplicador)
    print(Resultado)
  else:
    suma_de_control_acu((n/base),
              (sumaMultiplicadores - multiplicador),
              (suma +(multiplicador * (n%base))
            ))
print(suma_de_control_acu(2,1,3))
